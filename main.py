import mediapipe as mp
import cv2
import pyautogui
import win32api

def function(hand, points):
    normalized_landmark = hand.landmark[points]
    x, y = int(normalized_landmark.x * image_width), int(normalized_landmark.y * image_height)

    if points == mp_hands.HandLandmark.INDEX_FINGER_TIP:
        cv2.rectangle(image, (x - 12, y - 12), (x + 12, y + 12), (0, 200, 0), 5)
        win32api.SetCursorPos((x * 4, y * 5))
        pyautogui.mouseDown(button='left')


if __name__ == "__main__":

    mp_drawing = mp.solutions.drawing_utils
    mp_hands = mp.solutions.hands

    video = cv2.VideoCapture(0)

    hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.8,
                           min_tracking_confidence=0.5)

    pyautogui.FAILSAFE = False

    while True:
        ret, frame = video.read()
        if not ret:
            break

        image = cv2.flip(frame, 1)
        image_height, image_width, _ = image.shape
        results = hands.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

        if results.multi_hand_landmarks:
            hands_to_process = results.multi_hand_landmarks
            [function(hand, mp_hands.HandLandmark.INDEX_FINGER_TIP) for hand in hands_to_process]

        cv2.imshow('Dzien WEEIA', image)
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

    video.release()
    cv2.destroyAllWindows()
