document.addEventListener("DOMContentLoaded", () => { 
    const box = document.getElementById("box");
    const result = document.getElementById("result");
    const drawButton = document.getElementById("draw-button");
    const resetButton = document.getElementById("reset-button");
    var isShowButton = true;

    drawButton.addEventListener("click", () => {
        // 抽選ボックスを揺らすアニメーション
        box.classList.add("shake");
        result.innerHTML = "";

        setTimeout(() => {
            fetch("/draw")
                .then(response => response.json())
                .then(data => {
                    // 結果表示
                    const customText = document.createElement("span");
                    customText.textContent = "【おだい】";
                    customText.classList.add("result");
                    result.appendChild(customText);  // 【おだい】を追加
                    const br = document.createElement("br");
                    result.appendChild(br);
                    const textNode = document.createTextNode(data.result);
                    result.appendChild(textNode);
                    box.classList.remove("shake");

                    // 残り結果が1つの場合、ボタンを調整
                    if (data.remaining.length === 1) {
                        isShowButton = false;
                    }
                    drawButton.style.display = "none";
                    resetButton.style.display = "inline-block";

                });
        }, 1500);
    });

    resetButton.addEventListener("click", () => {
        fetch("/reset", { method: "POST" })
        result.textContent = "";
        if (isShowButton) {
            drawButton.style.display = "inline-block";
            resetButton.style.display = "none";
        } else {
            drawButton.style.display = "none";
            resetButton.style.display = "none";
        }
    });
});