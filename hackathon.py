import cv2
from ultralytics import YOLO

# Threshold minimal confidence
batas_confidence = 0.5
model = YOLO('best.pt')  # Model YOLO yang sudah dilatih

def detect_waste(frame):
    results = model(frame)
    return results

def main():
    cam = cv2.VideoCapture(0)  # kamera

    if not cam.isOpened():
        print("Error: kamera tidak aktif")
        exit()

    while True:
        ret, frame = cam.read()
        if not ret:
            print("Error: tidak dapat membaca frame")
            continue

        # Jalankan deteksi
        results = detect_waste(frame)

        # Loop semua hasil deteksi
        for result in results:
            boxes = result.boxes.xyxy.cpu().numpy()   # Bounding box (x1, y1, x2, y2)
            confidences = result.boxes.conf.cpu().numpy()  # Confidence
            labels = result.boxes.cls.cpu().numpy()        # Label index

            for i in range(len(boxes)):
                conf = confidences[i]
                if conf < batas_confidence:  # Skip kalau confidence kecil
                    continue

                bbox = boxes[i]
                label_index = int(labels[i])
                label = model.names[label_index]

                # Gambar bounding box
                cv2.rectangle(frame,
                              (int(bbox[0]), int(bbox[1])),
                              (int(bbox[2]), int(bbox[3])),
                              (0, 255, 0), 2)

                # Tampilkan label + confidence dalam persen
                text = f"{label} {conf*100:.2f}%"
                cv2.putText(frame, text,
                            (int(bbox[0]), int(bbox[1]) - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7,
                            (36, 255, 120), 2)

        # Tampilkan hasil di jendela kamera
        cv2.imshow("Waste Detection", frame)

        # Tekan ESC untuk keluar
        if cv2.waitKey(1) & 0xFF == 27:
            break

    cam.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
