import cv2
import numpy as np
from rect import Rect
from vector import Vector

def load_video_file(path: str):
  """
  Load a video file and get its metadata.

  Parameters:
      path (str): The file path of the video.

  Returns:
      Tuple[cv2.VideoCapture, dict]: A tuple containing the video object and a dictionary with video metadata.
          - The video object (cv2.VideoCapture) to read frames from the video file.
          - The metadata dictionary containing 'frame_rate', 'frame_width', and 'frame_height'.
  """
  video = cv2.VideoCapture(path)

  # Check if the video opened successfully
  if (video.isOpened() == False): 
    raise ("Error opening video file")

  metadata = {
    "frame_rate": video.get(cv2.CAP_PROP_FPS),
    "frame_count": video.get(cv2.CAP_PROP_FRAME_COUNT),
    "duration_secs": round(video.get(cv2.CAP_PROP_FRAME_COUNT) / video.get(cv2.CAP_PROP_FPS)),
    "frame_width": int(video.get(cv2.CAP_PROP_FRAME_WIDTH)),
    "frame_height": int(video.get(cv2.CAP_PROP_FRAME_HEIGHT)),
  }

  return video, metadata

def draw_rect_in_frame(frame, rect: Rect, colour: tuple, thickness: int = 2):
  """
  Draw a rectangle on the given frame.

  Parameters:
      frame (numpy.ndarray): The input frame on which to draw the rectangle.
      rect (Rect): The rectangle object defining the bounding box coordinates.
      colour (tuple): The color of the rectangle in BGR format (e.g., (0, 255, 0) for green).

  Returns:
      None
  """
  cv2.rectangle(frame, (rect.position.x, rect.position.y), (rect.position.x + rect.width, rect.position.y + rect.height), colour, thickness=thickness)

def draw_line_in_frame(frame, position_1: Vector, position_2: Vector, colour: tuple, thickness: int = 2):
  """
  Draw a line on the given frame.

  Parameters:
      frame (numpy.ndarray): The input frame on which to draw the rectangle.
      rect (Rect): The rectangle object defining the bounding box coordinates.
      colour (tuple): The color of the rectangle in BGR format (e.g., (0, 255, 0) for green).

  Returns:
      None
  """
  cv2.line(frame, (position_1.x, position_1.y), (position_2.x, position_2.y), colour, thickness=thickness)

def draw_text_in_frame(frame, text: str, position: Vector, colour: tuple, font_scale: float = 0.5, thickness: int = 2):
  """
  Draw text on the given frame.

  Parameters:
      frame (numpy.ndarray): The input frame on which to draw the rectangle.
      rect (Rect): The rectangle object defining the bounding box coordinates.
      colour (tuple): The color of the rectangle in BGR format (e.g., (0, 255, 0) for green).

  Returns:
      None
  """
  cv2.putText(frame, text, (position.x, position.y), cv2.FONT_HERSHEY_SIMPLEX, font_scale, colour, thickness)

def get_median_frame(file_path: str, num_samples=50):
  """
  Calculate the median of randomly selected frames from the video.

  Parameters:
      file_path (str): The file path of the video.
      num_samples (int): The number of frames to randomly select for calculating the median (default: 50).

  Returns:
      numpy.ndarray: The background frame as a numpy array.
  """
  video = cv2.VideoCapture(file_path)
  
  # Randomly select 50 frames for the calculating the median
  frame_indices = video.get(cv2.CAP_PROP_FRAME_COUNT) * np.random.uniform(size=num_samples)
  
  # Store the frames in array
  frames = []
  for idx in frame_indices:
    # set the frame id to read that particular frame
    video.set(cv2.CAP_PROP_POS_FRAMES, idx)
    ret, frame = video.read()
    frames.append(frame)

  # Calculate the median of all the frames
  median_frame = np.median(frames, axis=0).astype(np.uint8)

  return median_frame

def subtract_background(background_frame, current_frame):
  """
  Subtract the background frame from the current frame.

  Parameters:
      background_frame (numpy.ndarray): The background frame as a numpy array.
      current_frame (numpy.ndarray): The current frame as a numpy array.

  Returns:
      numpy.ndarray: The subtracted frame as a numpy array.
  """
  # Ensure both frames have the same size (width and height)
  if background_frame.shape[:2] != current_frame.shape[:2]:
      raise ValueError("Background and current frames must have the same size.")

  # Compute the absolute difference between the two frames
  diff_frame = cv2.absdiff(background_frame, current_frame)

  return diff_frame
