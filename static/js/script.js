// Upload Image
function uploadImage() {
    let fileInput = document.getElementById("imageInput");
    let file = fileInput.files[0];

    let formData = new FormData();
    formData.append("image", file);

    fetch("/upload", {
        method: "POST",
        body: formData
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById("preview").src = data.image;
        document.getElementById("result").innerText =
            "Emotion: " + data.emotion + " (" + data.score + ")";
    });
}

// Webcam
let video = document.getElementById("video");

function startWebcam() {
    navigator.mediaDevices.getUserMedia({ video: true })
    .then(stream => {
        video.srcObject = stream;
        detectFrame();
    });
}

function detectFrame() {
    let canvas = document.createElement("canvas");
    let ctx = canvas.getContext("2d");

    setInterval(() => {
        canvas.width = video.videoWidth;
        canvas.height = video.videoHeight;

        ctx.drawImage(video, 0, 0);

        canvas.toBlob(blob => {
            let formData = new FormData();
            formData.append("frame", blob);

            fetch("/webcam", {
                method: "POST",
                body: formData
            })
            .then(res => res.json())
            .then(data => {
                document.getElementById("liveResult").innerText =
                    "Live Emotion: " + data.emotion + " (" + data.score + ")";
            });
        });
    }, 2000); // every 2 sec
}