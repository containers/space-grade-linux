import pyrealsense2 as rs
import numpy as np
import cv2

class Intel435iManager:
    def __init__(self):
        """Initialize the Intel 435i camera pipeline and configuration."""
        self.pipeline = rs.pipeline()
        self.config = rs.config()
        self.running = False

    def initialize(self, width=640, height=480, fps=30):
        """Configure the camera stream."""
        self.config.enable_stream(rs.stream.depth, width, height, rs.format.z16, fps)
        self.config.enable_stream(rs.stream.color, width, height, rs.format.bgr8, fps)
        print("Camera initialized.")

    def start(self):
        """Start the camera pipeline."""
        try:
            self.pipeline.start(self.config)
            self.running = True
            print("Camera started.")
        except Exception as e:
            print(f"Error starting the camera: {e}")

    def stop(self):
        """Stop the camera pipeline."""
        if self.running:
            self.pipeline.stop()
            self.running = False
            print("Camera stopped.")

    def get_frames(self):
        """Capture a single frame of depth and color data."""
        if not self.running:
            print("Camera is not running. Start the camera first.")
            return None, None, None

        try:
            frames = self.pipeline.wait_for_frames()
            depth_frame = frames.get_depth_frame()
            color_frame = frames.get_color_frame()

            if not depth_frame or not color_frame:
                print("Failed to capture frames.")
                return None, None, None

            depth_image = np.asanyarray(depth_frame.get_data())
            color_image = np.asanyarray(color_frame.get_data())
            return depth_frame, depth_image, color_image
        except Exception as e:
            print(f"Error capturing frames: {e}")
            return None, None, None

    def get_distance(self, depth_frame, x, y):
        """
        Get the distance at a specific pixel (x, y).
        
        Parameters:
            depth_frame (rs.frame): The depth frame from which to extract distance.
            x (int): The x-coordinate of the pixel.
            y (int): The y-coordinate of the pixel.
        
        Returns:
            float: The distance in meters at the given pixel.
        """
        if not depth_frame:
            print("Invalid depth frame.")
            return None
        distance = depth_frame.get_distance(x, y)
        return distance

    def save_snapshot(self, color_image, depth_image=None, save_depth=False, color_path="color_snapshot.png", depth_path="depth_snapshot.png"):
        """
        Save color and optionally depth images as snapshots.
        
        Parameters:
            color_image (np.ndarray): The color image to save.
            depth_image (np.ndarray): The depth image to save (optional).
            save_depth (bool): Whether to save the depth image. Default is False.
            color_path (str): Path to save the color image.
            depth_path (str): Path to save the depth image (if enabled).
        """
        try:
            # Save the color image
            cv2.imwrite(color_path, color_image)
            print(f"Color snapshot saved as {color_path}.")

            # Save the depth image only if requested
            if save_depth and depth_image is not None:
                normalized_depth = cv2.normalize(depth_image, None, 0, 255, cv2.NORM_MINMAX)
                normalized_depth = cv2.convertScaleAbs(normalized_depth)
                cv2.imwrite(depth_path, normalized_depth)
                print(f"Depth snapshot saved as {depth_path}.")
        except Exception as e:
            print(f"Error saving snapshots: {e}")

    def convert_to_readable_units(self, distance_in_meters):
        """
        Convert distance from meters to human-readable units.
        
        Parameters:
            distance_in_meters (float): The distance in meters.
        
        Returns:
            dict: A dictionary with distances in meters, centimeters, and inches.
        """
        return {
            "meters": round(distance_in_meters, 3),
            "centimeters": round(distance_in_meters * 100, 1),
            "inches": round(distance_in_meters * 39.3701, 2)
        }

    def __del__(self):
        """Ensure the camera pipeline is stopped when the object is deleted."""
        if self.running:
            self.stop()

# Example of usage
#if __name__ == "__main__":
#    camera = Intel435iManager()
#
#    # Initialize camera
#    camera.initialize()
#
#    # Start camera
#    camera.start()
#
    # Capture frames
#    depth_frame, depth_image, color_image = camera.get_frames()
#
#    if depth_frame:
#        # Get distance at specific points (e.g., center of the frame)
#        height, width = depth_image.shape
#        center_x, center_y = width // 2, height // 2
#
#        center_distance = camera.get_distance(depth_frame, center_x, center_y)
#        if center_distance > 0:  # Check if the distance is valid
#            center_readable = camera.convert_to_readable_units(center_distance)
#            print(f"Distance at center ({center_x}, {center_y}): {center_readable}")
#        else:
#            print(f"Distance at center ({center_x}, {center_y}) is out of range.")
#
        # Save color snapshot; depth snapshot is optional
#        camera.save_snapshot(color_image, depth_image, save_depth=False)
#
    # Stop the camera
#    camera.stop()
