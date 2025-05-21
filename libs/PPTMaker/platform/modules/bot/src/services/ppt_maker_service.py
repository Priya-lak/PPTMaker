import json
import logging
from typing import List, Dict, Any, Tuple, Optional
import uuid

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.oauth2.service_account import Credentials
from libs.utils.common.custom_logger import CustomLogger
from libs.utils.common.file_helpers.helpers import read_json_file

log = CustomLogger("GroqLLMService", is_request=False)

logger, listener = log.get_logger()

listener.start()


class PresentationMaker():
    def __init__(self):
        self.credentials = Credentials.from_service_account_info(
            read_json_file("creds.json"),
            scopes=[
                "https://www.googleapis.com/auth/presentations",
                "https://www.googleapis.com/auth/drive",
            ],
        )
        self.slide_service = None
        self.drive_service = None
        self._initialize_services()

    def _initialize_services(self):
        """Initialize Google API services."""
        try:
            self.slide_service = build("slides", "v1", credentials=self.credentials)
            self.drive_service = build("drive", "v3", credentials=self.credentials)
            logger.info("Google API services initialized successfully")
        except Exception as e:
            logger.error(f"Error initializing Google API services: {e}")
            raise

    def create_presentation(self, title):
        """
        Creates a new presentation.

        Args:
            title (str): The title of the presentation

        Returns:
            dict: The presentation object with ID and other details
        """
        try:
            logger.info(f"Creating presentation: '{title}'")
            body = {"title": title}
            presentation = (
                self.slide_service.presentations().create(body=body).execute()
            )
            presentation_id = presentation.get("presentationId")
            logger.info(f"Created presentation with ID: {presentation_id}")
            return presentation
        except HttpError as api_error:
            logger.error(f"Google API error: {api_error}")
            logger.error(f"Response status: {api_error.resp.status}")
            logger.error(f"Response content: {api_error.content}")
            return None
        except Exception as error:
            logger.error(
                f"Unexpected error creating presentation: {error}", exc_info=True
            )
            return None

    def share_presentation(self, email, presentation_id):
        """
        Shares the presentation with the specified email address.

        Args:
            email (str): The email address to share with
            presentation_id (str): The ID of the presentation to share

        Returns:
            bool: True if successful, False otherwise
        """
        try:
            logger.info(f"Sharing presentation {presentation_id} with {email}")

            # Create permission
            user_permission = {
                "type": "user",
                "role": "writer",  # Can be 'reader', 'writer', 'commenter'
                "emailAddress": email,
            }

            # Add the permission to the file
            self.drive_service.permissions().create(
                fileId=presentation_id,
                body=user_permission,
                fields="id",
                sendNotificationEmail=True,
            ).execute()

            logger.info(f"Successfully shared presentation with {email}")
            return True
        except HttpError as error:
            logger.error(f"Error sharing presentation: {error}")
            return False
        except Exception as error:
            logger.error(
                f"Unexpected error sharing presentation: {error}", exc_info=True
            )
            return False

    def create_slide(self, presentation_id, layout="TITLE_AND_BODY"):
        """
        Creates a new slide in the presentation.

        Args:
            presentation_id (str): The ID of the presentation
            layout (str): The slide layout predefined layout type
                         (see https://developers.google.com/slides/api/reference/rest/v1/presentations.pages#Layout)

        Returns:
            str: The object ID of the created slide
        """
        try:
            # Define the slide layout
            

            # Create the slide
            requests = [
                {
                    "createSlide": {
                        "objectId": str(uuid.uuid4()),
                        "insertionIndex": "1",
                        "slideLayoutReference": {
                            "predefinedLayout": "TITLE_AND_TWO_COLUMNS"
                        },
                    }
                }
            ]

            # If you wish to populate the slide with elements,
            # add element create requests here, using the page_id.

            # Execute the request.
            body = {"requests": requests}
            response = (
                self.slide_service.presentations()
                .batchUpdate(presentationId=presentation_id, body=body)
                .execute()
            )
            create_slide_response = response.get("replies")[0].get("createSlide")
            slide_id= create_slide_response.get('objectId')
            logger.info(f"Created slide with ID: {slide_id}")

            return slide_id
        except Exception as e:
            logger.error(f"Error creating slide: {e}")
            return None

    def add_text_box(
        self,
        presentation_id,
        slide_id,
        text,
        x=100,
        y=100,
        width=400,
        height=100,
        font_size=14,
        bold=False,
        italic=False,
        color=None,
    ):
        """
        Adds a text box to a slide.

        Args:
            presentation_id (str): The ID of the presentation
            slide_id (str): The ID of the slide
            text (str): The text content
            x, y (float): Position coordinates (in points)
            width, height (float): Size dimensions (in points)
            font_size (int): Text font size
            bold (bool): Whether text should be bold
            italic (bool): Whether text should be italic
            color (dict): Text color in RGB format, e.g., {"red": 0.5, "green": 0.5, "blue": 0.5}

        Returns:
            str: The object ID of the created text box
        """
        try:
            # Generate a unique ID for the text box
            text_box_id = f"textbox_{slide_id}_{hash(text) % 10000}"

            # Define the text box
            requests = [
                {
                    "createShape": {
                        "objectId": text_box_id,
                        "shapeType": "TEXT_BOX",
                        "elementProperties": {
                            "pageObjectId": slide_id,
                            "size": {
                                "width": {"magnitude": width, "unit": "PT"},
                                "height": {"magnitude": height, "unit": "PT"},
                            },
                            "transform": {
                                "scaleX": 1,
                                "scaleY": 1,
                                "translateX": x,
                                "translateY": y,
                                "unit": "PT",
                            },
                        },
                    }
                },
                {"insertText": {"objectId": text_box_id, "text": text}},
            ]

            # Add text styling if specified
            style_requests = []
            if font_size or bold or italic or color:
                style_request = {
                    "updateTextStyle": {
                        "objectId": text_box_id,
                        "textRange": {"type": "ALL"},
                        "style": {},
                        "fields": "",
                    }
                }

                if font_size:
                    style_request["updateTextStyle"]["style"]["fontSize"] = {
                        "magnitude": font_size,
                        "unit": "PT",
                    }
                    style_request["updateTextStyle"]["fields"] += "fontSize,"

                if bold:
                    style_request["updateTextStyle"]["style"]["bold"] = True
                    style_request["updateTextStyle"]["fields"] += "bold,"

                if italic:
                    style_request["updateTextStyle"]["style"]["italic"] = True
                    style_request["updateTextStyle"]["fields"] += "italic,"

                if color:
                    style_request["updateTextStyle"]["style"]["foregroundColor"] = {
                        "opaqueColor": {"rgbColor": color}
                    }
                    style_request["updateTextStyle"]["fields"] += "foregroundColor,"

                # Remove trailing comma
                style_request["updateTextStyle"]["fields"] = style_request[
                    "updateTextStyle"
                ]["fields"].rstrip(",")
                style_requests.append(style_request)

            # Execute the requests
            all_requests = requests + style_requests
            self.slide_service.presentations().batchUpdate(
                presentationId=presentation_id, body={"requests": all_requests}
            ).execute()

            logger.info(f"Added text box to slide {slide_id}")
            return text_box_id
        except Exception as e:
            logger.error(f"Error adding text box: {e}")
            return None

    def add_title(self, presentation_id, slide_id, title_text):
        """
        Adds a title to a slide by finding the title placeholder.

        Args:
            presentation_id (str): The ID of the presentation
            slide_id (str): The ID of the slide
            title_text (str): The title text

        Returns:
            bool: True if successful, False otherwise
        """
        try:
            # Get the slide details to find the title placeholder
            slide = (
                self.slide_service.presentations()
                .pages()
                .get(presentationId=presentation_id, pageObjectId=slide_id)
                .execute()
            )

            # Find the title placeholder
            title_placeholder_id = None
            for element in slide.get("pageElements", []):
                if (
                    element.get("shape", {}).get("placeholder", {}).get("type")
                    == "TITLE"
                ):
                    title_placeholder_id = element.get("objectId")
                    break

            if not title_placeholder_id:
                logger.warning(f"No title placeholder found on slide {slide_id}")
                # If no placeholder found, create a text box at the top as a title
                return self.add_text_box(
                    presentation_id,
                    slide_id,
                    title_text,
                    x=100,
                    y=50,
                    width=600,
                    height=60,
                    font_size=24,
                    bold=True,
                )

            # Insert text into the title placeholder
            requests = [
                {"insertText": {"objectId": title_placeholder_id, "text": title_text}}
            ]

            self.slide_service.presentations().batchUpdate(
                presentationId=presentation_id, body={"requests": requests}
            ).execute()

            logger.info(f"Added title to slide {slide_id}")
            return True
        except Exception as e:
            logger.error(f"Error adding title: {e}")
            return False

    def add_body_text(self, presentation_id, slide_id, body_text):
        """
        Adds body text to a slide by finding the body placeholder.

        Args:
            presentation_id (str): The ID of the presentation
            slide_id (str): The ID of the slide
            body_text (str): The body text

        Returns:
            bool: True if successful, False otherwise
        """
        try:
            # Get the slide details to find the body placeholder
            slide = (
                self.slide_service.presentations()
                .pages()
                .get(presentationId=presentation_id, pageObjectId=slide_id)
                .execute()
            )

            # Find the body placeholder
            body_placeholder_id = None
            for element in slide.get("pageElements", []):
                if (
                    element.get("shape", {}).get("placeholder", {}).get("type")
                    == "BODY"
                ):
                    body_placeholder_id = element.get("objectId")
                    break

            if not body_placeholder_id:
                logger.warning(f"No body placeholder found on slide {slide_id}")
                # If no placeholder found, create a text box below the title area
                return self.add_text_box(
                    presentation_id,
                    slide_id,
                    body_text,
                    x=100,
                    y=150,
                    width=600,
                    height=300,
                    font_size=14,
                )

            # Insert text into the body placeholder
            requests = [
                {"insertText": {"objectId": body_placeholder_id, "text": body_text}}
            ]

            self.slide_service.presentations().batchUpdate(
                presentationId=presentation_id, body={"requests": requests}
            ).execute()

            logger.info(f"Added body text to slide {slide_id}")
            return True
        except Exception as e:
            logger.error(f"Error adding body text: {e}")
            return False

    def add_image_url(
        self, presentation_id, slide_id, image_url, x=100, y=100, width=300, height=200
    ):
        """
        Adds an image from a URL to a slide.

        Args:
            presentation_id (str): The ID of the presentation
            slide_id (str): The ID of the slide
            image_url (str): The URL of the image
            x, y (float): Position coordinates (in points)
            width, height (float): Size dimensions (in points)

        Returns:
            str: The object ID of the created image
        """
        try:
            # Generate a unique ID for the image
            image_id = f"image_{slide_id}_{hash(image_url) % 10000}"

            # Create the image
            requests = [
                {
                    "createImage": {
                        "objectId": image_id,
                        "url": image_url,
                        "elementProperties": {
                            "pageObjectId": slide_id,
                            "size": {
                                "width": {"magnitude": width, "unit": "PT"},
                                "height": {"magnitude": height, "unit": "PT"},
                            },
                            "transform": {
                                "scaleX": 1,
                                "scaleY": 1,
                                "translateX": x,
                                "translateY": y,
                                "unit": "PT",
                            },
                        },
                    }
                }
            ]

            self.slide_service.presentations().batchUpdate(
                presentationId=presentation_id, body={"requests": requests}
            ).execute()

            logger.info(f"Added image to slide {slide_id}")
            return image_id
        except Exception as e:
            logger.error(f"Error adding image: {e}")
            return None

    def add_shape(
        self,
        presentation_id,
        slide_id,
        shape_type="RECTANGLE",
        x=100,
        y=100,
        width=200,
        height=100,
        fill_color=None,
        border_color=None,
    ):
        """
        Adds a shape to a slide.

        Args:
            presentation_id (str): The ID of the presentation
            slide_id (str): The ID of the slide
            shape_type (str): The type of shape (RECTANGLE, ELLIPSE, etc.)
            x, y (float): Position coordinates (in points)
            width, height (float): Size dimensions (in points)
            fill_color (dict): Fill color in RGB format, e.g., {"red": 0.5, "green": 0.5, "blue": 0.5}
            border_color (dict): Border color in RGB format

        Returns:
            str: The object ID of the created shape
        """
        try:
            # Generate a unique ID for the shape
            shape_id = f"shape_{slide_id}_{hash(shape_type) % 10000}"

            # Define the shape request
            requests = [
                {
                    "createShape": {
                        "objectId": shape_id,
                        "shapeType": shape_type,
                        "elementProperties": {
                            "pageObjectId": slide_id,
                            "size": {
                                "width": {"magnitude": width, "unit": "PT"},
                                "height": {"magnitude": height, "unit": "PT"},
                            },
                            "transform": {
                                "scaleX": 1,
                                "scaleY": 1,
                                "translateX": x,
                                "translateY": y,
                                "unit": "PT",
                            },
                        },
                    }
                }
            ]

            # Add styling if specified
            style_requests = []
            if fill_color or border_color:
                style_request = {
                    "updateShapeProperties": {
                        "objectId": shape_id,
                        "shapeProperties": {},
                        "fields": "",
                    }
                }

                if fill_color:
                    style_request["updateShapeProperties"]["shapeProperties"][
                        "fill"
                    ] = {"solidFill": {"color": {"rgbColor": fill_color}}}
                    style_request["updateShapeProperties"]["fields"] += "fill,"

                if border_color:
                    style_request["updateShapeProperties"]["shapeProperties"][
                        "outline"
                    ] = {
                        "outlineFill": {
                            "solidFill": {"color": {"rgbColor": border_color}}
                        },
                        "weight": {"magnitude": 1, "unit": "PT"},
                    }
                    style_request["updateShapeProperties"]["fields"] += "outline,"

                # Remove trailing comma
                style_request["updateShapeProperties"]["fields"] = style_request[
                    "updateShapeProperties"
                ]["fields"].rstrip(",")
                style_requests.append(style_request)

            # Execute the requests
            all_requests = requests + style_requests
            self.slide_service.presentations().batchUpdate(
                presentationId=presentation_id, body={"requests": all_requests}
            ).execute()

            logger.info(f"Added shape to slide {slide_id}")
            return shape_id
        except Exception as e:
            logger.error(f"Error adding shape: {e}")
            return None

    def add_bullet_list(
        self, presentation_id, slide_id, items, x=100, y=150, width=600, height=300
    ):
        """
        Adds a bullet list to a slide.

        Args:
            presentation_id (str): The ID of the presentation
            slide_id (str): The ID of the slide
            items (list): List of bullet point items
            x, y (float): Position coordinates (in points)
            width, height (float): Size dimensions (in points)

        Returns:
            str: The object ID of the created bullet list
        """
        try:
            # Generate a unique ID for the text box
            list_id = f"list_{slide_id}_{hash(str(items)) % 10000}"

            # Format the bullet list text
            bullet_text = "\n".join(items)

            # Create the text box
            requests = [
                {
                    "createShape": {
                        "objectId": list_id,
                        "shapeType": "TEXT_BOX",
                        "elementProperties": {
                            "pageObjectId": slide_id,
                            "size": {
                                "width": {"magnitude": width, "unit": "PT"},
                                "height": {"magnitude": height, "unit": "PT"},
                            },
                            "transform": {
                                "scaleX": 1,
                                "scaleY": 1,
                                "translateX": x,
                                "translateY": y,
                                "unit": "PT",
                            },
                        },
                    }
                },
                {"insertText": {"objectId": list_id, "text": bullet_text}},
            ]

            # Apply bullet styling to each paragraph
            bullet_requests = []
            for i in range(len(items)):
                start_index = 0 if i == 0 else sum(len(items[j]) for j in range(i)) + i
                end_index = start_index + len(items[i])

                bullet_request = {
                    "createParagraphBullets": {
                        "objectId": list_id,
                        "textRange": {"startIndex": start_index, "endIndex": end_index},
                        "bulletPreset": "BULLET_DISC_CIRCLE_SQUARE",
                    }
                }
                bullet_requests.append(bullet_request)

            # Execute the requests
            all_requests = requests + bullet_requests
            self.slide_service.presentations().batchUpdate(
                presentationId=presentation_id, body={"requests": all_requests}
            ).execute()

            logger.info(f"Added bullet list to slide {slide_id}")
            return list_id
        except Exception as e:
            logger.error(f"Error adding bullet list: {e}")
            return None

    def add_chart(
        self,
        presentation_id,
        slide_id,
        chart_data,
        chart_type="BAR",
        x=100,
        y=100,
        width=400,
        height=300,
    ):
        """
        Adds a chart to a slide.

        Args:
            presentation_id (str): The ID of the presentation
            slide_id (str): The ID of the slide
            chart_data (dict): Chart data structured according to Google Slides API
                              (see API docs for specific format)
            chart_type (str): Chart type (BAR, LINE, PIE, etc.)
            x, y (float): Position coordinates (in points)
            width, height (float): Size dimensions (in points)

        Returns:
            str: The object ID of the created chart
        """
        try:
            # Generate a unique ID for the chart
            chart_id = f"chart_{slide_id}_{hash(chart_type) % 10000}"

            # Create the chart
            requests = [
                {
                    "createSheetsChart": {
                        "objectId": chart_id,
                        "spreadsheetId": chart_data.get("spreadsheetId"),
                        "chartId": chart_data.get("chartId"),
                        "linkingMode": "LINKED",
                        "elementProperties": {
                            "pageObjectId": slide_id,
                            "size": {
                                "width": {"magnitude": width, "unit": "PT"},
                                "height": {"magnitude": height, "unit": "PT"},
                            },
                            "transform": {
                                "scaleX": 1,
                                "scaleY": 1,
                                "translateX": x,
                                "translateY": y,
                                "unit": "PT",
                            },
                        },
                    }
                }
            ]

            self.slide_service.presentations().batchUpdate(
                presentationId=presentation_id, body={"requests": requests}
            ).execute()

            logger.info(f"Added chart to slide {slide_id}")
            return chart_id
        except Exception as e:
            logger.error(f"Error adding chart: {e}")
            return None

    def add_table(
        self,
        presentation_id,
        slide_id,
        rows,
        cols,
        data,
        x=100,
        y=100,
        width=400,
        height=300,
    ):
        """
        Adds a table to a slide.

        Args:
            presentation_id (str): The ID of the presentation
            slide_id (str): The ID of the slide
            rows (int): Number of rows
            cols (int): Number of columns
            data (list): 2D list of cell data [[row1_col1, row1_col2...], [row2_col1, row2_col2...], ...]
            x, y (float): Position coordinates (in points)
            width, height (float): Size dimensions (in points)

        Returns:
            str: The object ID of the created table
        """
        try:
            # Generate a unique ID for the table
            table_id = f"table_{slide_id}_{hash(str(data)) % 10000}"

            # Create the table
            requests = [
                {
                    "createTable": {
                        "objectId": table_id,
                        "rows": rows,
                        "columns": cols,
                        "elementProperties": {
                            "pageObjectId": slide_id,
                            "size": {
                                "width": {"magnitude": width, "unit": "PT"},
                                "height": {"magnitude": height, "unit": "PT"},
                            },
                            "transform": {
                                "scaleX": 1,
                                "scaleY": 1,
                                "translateX": x,
                                "translateY": y,
                                "unit": "PT",
                            },
                        },
                    }
                }
            ]

            # Execute the create table request
            self.slide_service.presentations().batchUpdate(
                presentationId=presentation_id, body={"requests": requests}
            ).execute()

            # Populate the table cells
            cell_requests = []
            for i in range(min(rows, len(data))):
                for j in range(min(cols, len(data[i]) if i < len(data) else 0)):
                    cell_content = (
                        str(data[i][j]) if i < len(data) and j < len(data[i]) else ""
                    )

                    insert_text_request = {
                        "insertText": {
                            "objectId": table_id,
                            "cellLocation": {"rowIndex": i, "columnIndex": j},
                            "text": cell_content,
                        }
                    }
                    cell_requests.append(insert_text_request)

            if cell_requests:
                self.slide_service.presentations().batchUpdate(
                    presentationId=presentation_id, body={"requests": cell_requests}
                ).execute()

            logger.info(f"Added table to slide {slide_id}")
            return table_id
        except Exception as e:
            logger.error(f"Error adding table: {e}")
            return None

    def apply_slide_theme(self, presentation_id, theme_id=None):
        """
        Applies a theme to the presentation.

        Args:
            presentation_id (str): The ID of the presentation
            theme_id (str): The ID of the theme to apply

        Returns:
            bool: True if successful, False otherwise
        """
        try:
            # If no theme_id provided, use a default theme
            if not theme_id:
                # Unfortunately, direct theme application requires the theme to exist
                # In a real implementation, you might have a set of predefined themes
                logger.warning("Direct theme application requires an existing theme ID")
                return False

            requests = [{"applyTheme": {"themeId": theme_id}}]

            self.slide_service.presentations().batchUpdate(
                presentationId=presentation_id, body={"requests": requests}
            ).execute()

            logger.info(f"Applied theme to presentation {presentation_id}")
            return True
        except Exception as e:
            logger.error(f"Error applying theme: {e}")
            return False

    def add_speaker_notes(self, presentation_id, slide_id, notes):
        """
        Adds speaker notes to a slide.

        Args:
            presentation_id (str): The ID of the presentation
            slide_id (str): The ID of the slide
            notes (str): The speaker notes text

        Returns:
            bool: True if successful, False otherwise
        """
        try:
            requests = [
                {
                    "insertText": {
                        "objectId": slide_id,
                        "insertionIndex": 0,
                        "text": notes,
                    }
                }
            ]

            self.slide_service.presentations().batchUpdate(
                presentationId=presentation_id, body={"requests": requests}
            ).execute()

            logger.info(f"Added speaker notes to slide {slide_id}")
            return True
        except Exception as e:
            logger.error(f"Error adding speaker notes: {e}")
            return False

    def delete_slide(self, presentation_id, slide_id):
        """
        Deletes a slide from the presentation.

        Args:
            presentation_id (str): The ID of the presentation
            slide_id (str): The ID of the slide to delete

        Returns:
            bool: True if successful, False otherwise
        """
        try:
            requests = [{"deleteObject": {"objectId": slide_id}}]

            self.slide_service.presentations().batchUpdate(
                presentationId=presentation_id, body={"requests": requests}
            ).execute()

            logger.info(f"Deleted slide {slide_id}")
            return True
        except Exception as e:
            logger.error(f"Error deleting slide: {e}")
            return False

    def move_slide(self, presentation_id, slide_id, new_position):
        """
        Moves a slide to a new position in the presentation.

        Args:
            presentation_id (str): The ID of the presentation
            slide_id (str): The ID of the slide to move
            new_position (int): The new position index (0-based)

        Returns:
            bool: True if successful, False otherwise
        """
        try:
            requests = [
                {
                    "updateSlidesPosition": {
                        "slideObjectIds": [slide_id],
                        "insertionIndex": new_position,
                    }
                }
            ]

            self.slide_service.presentations().batchUpdate(
                presentationId=presentation_id, body={"requests": requests}
            ).execute()

            logger.info(f"Moved slide {slide_id} to position {new_position}")
            return True
        except Exception as e:
            logger.error(f"Error moving slide: {e}")
            return False

    def export_pdf(self, presentation_id, output_file="presentation.pdf"):
        """
        Exports the presentation as a PDF file.

        Args:
            presentation_id (str): The ID of the presentation
            output_file (str): The output file path

        Returns:
            bool: True if successful, False otherwise
        """
        try:
            # Export presentation as PDF
            response = (
                self.drive_service.files()
                .export(fileId=presentation_id, mimeType="application/pdf")
                .execute()
            )

            # Save the PDF
            with open(output_file, "wb") as f:
                f.write(response)

            logger.info(f"Exported presentation to {output_file}")
            return True
        except Exception as e:
            logger.error(f"Error exporting presentation as PDF: {e}")
            return False


# Example usage class
class PresentationAI:
    def __init__(self):
        """Initialize the PresentationAI which uses the PresentationMaker."""
        self.maker = PresentationMaker()

    def create_simple_presentation(self, title, content_data):
        """
        Creates a simple presentation with title slide and content slides.

        Args:
            title (str): The title of the presentation
            content_data (list): List of dictionaries containing slide data
                                [{"title": "Slide Title", "content": "Slide content or bullet points list"}]

        Returns:
            str: The ID of the created presentation
        """
        # Create the presentation
        presentation = self.maker.create_presentation(title)
        if not presentation:
            logger.error("Failed to create presentation")
            return None

        presentation_id = presentation.get("presentationId")

        # Create title slide
        title_slide_id = self.maker.create_slide(presentation_id, layout="TITLE")
        self.maker.add_title(presentation_id, title_slide_id, title)
        self.maker.add_text_box(
            presentation_id,
            title_slide_id,
            "Created with PowerPoint Maker AI",
            x=200,
            y=350,
            width=400,
            height=50,
            font_size=12,
            italic=True,
            color={"red": 0.5, "green": 0.5, "blue": 0.5},
        )

        # Create content slides
        for slide_data in content_data:
            slide_title = slide_data.get("title", "Untitled Slide")
            slide_content = slide_data.get("content", "")

            # Create slide
            slide_id = self.maker.create_slide(presentation_id, layout="TITLE_AND_BODY")
            self.maker.add_title(presentation_id, slide_id, slide_title)

            # Check if content is a list or string
            if isinstance(slide_content, list):
                self.maker.add_bullet_list(presentation_id, slide_id, slide_content)
            else:
                self.maker.add_body_text(presentation_id, slide_id, slide_content)

        logger.info(
            f"Created presentation '{title}' with {len(content_data) + 1} slides"
        )
        return presentation_id

    def create_data_presentation(
        self, title, chart_data, table_data=None, share_with=None
    ):
        """
        Creates a data-focused presentation with charts and tables.

        Args:
            title (str): The title of the presentation
            chart_data (dict): Data for charts including spreadsheet ID and chart ID
            table_data (list): List of tables to include [{"title": "Table Title", "data": [[row1], [row2]]}]
            share_with (str): Email to share the presentation with (optional)

        Returns:
            str: The ID of the created presentation
        """
        # Create the presentation
        presentation = self.maker.create_presentation(title)
        if not presentation:
            logger.error("Failed to create presentation")
            return None

        presentation_id = presentation.get("presentationId")

        # Create title slide
        title_slide_id = self.maker.create_slide(presentation_id, layout="TITLE")
        self.maker.add_title(presentation_id, title_slide_id, title)
        self.maker.add_text_box(
            presentation_id,
            title_slide_id,
            "Data Visualization Presentation",
            x=200,
            y=350,
            width=400,
            height=50,
            font_size=16,
            italic=True,
        )

        # Add chart slide
        chart_slide_id = self.maker.create_slide(
            presentation_id, layout="TITLE_AND_CONTENT"
        )
        self.maker.add_title(presentation_id, chart_slide_id, "Data Analysis")
        self.maker.add_chart(
            presentation_id,
            chart_slide_id,
            chart_data,
            x=100,
            y=100,
            width=500,
            height=300,
        )

        # Add table slides if provided
        if table_data:
            for table_info in table_data:
                table_title = table_info.get("title", "Data Table")
                table_rows = table_info.get("data", [])

                if not table_rows:
                    continue

                table_slide_id = self.maker.create_slide(
                    presentation_id, layout="TITLE_AND_CONTENT"
                )
                self.maker.add_title(presentation_id, table_slide_id, table_title)

                rows = len(table_rows)
                cols = len(table_rows[0]) if rows > 0 else 0

                if rows > 0 and cols > 0:
                    self.maker.add_table(
                        presentation_id,
                        table_slide_id,
                        rows,
                        cols,
                        table_rows,
                        x=50,
                        y=100,
                        width=600,
                        height=300,
                    )

        # Share the presentation if an email is provided
        if share_with:
            self.maker.share_presentation(share_with, presentation_id)
            logger.info(f"Shared presentation with {share_with}")

        logger.info(f"Created data presentation with ID: {presentation_id}")
        return presentation_id

# Example use of the PowerPoint Maker AI
if __name__ == "__main__":
    # Initialize the AI
    ppt_ai = PresentationAI()

    # Example 1: Create a simple presentation
    simple_content = [
        {
            "title": "Introduction",
            "content": "This is a simple presentation created with Python.",
        },
        {
            "title": "Features",
            "content": [
                "Automatic slide creation",
                "Text formatting",
                "Images and shapes",
                "Tables and charts",
                "PDF export capability",
            ],
        },
        {
            "title": "Conclusion",
            "content": "Thank you for using our PowerPoint Maker AI!",
        },
    ]

    simple_ppt_id = ppt_ai.create_simple_presentation(
        "Demo Presentation", simple_content
    )

    # Example 2: Create a data presentation (assuming you have Google Sheets charts)
    # Note: This requires a Google Sheet with charts already created
    chart_data = {
        "spreadsheetId": "your_spreadsheet_id",  # Replace with actual ID
        "chartId": 1234,  # Replace with actual chart ID
    }

    table_data = [
        {
            "title": "Sales Data",
            "data": [
                ["Region", "Q1", "Q2", "Q3", "Q4"],
                ["North", 10000, 12000, 15000, 18000],
                ["South", 8000, 9000, 10000, 12000],
                ["East", 12000, 13000, 14000, 15000],
                ["West", 9000, 10000, 11000, 13000],
            ],
        }
    ]

    data_ppt_id = ppt_ai.create_data_presentation(
        "Quarterly Sales Report",
        chart_data,
        table_data,
        share_with="priyalakhani91@gmail.com",  # Optional
    )

    # Example 3: Create a marketing presentation
    brand_color = {"red": 0.2, "green": 0.6, "blue": 0.9}  # Blue-ish color
