var buildUrl = "";
var loaderUrl = buildUrl + "website_game/static/src/game/UE4Game/myproject1html/Build/myproject1html.loader.js";
var config = {
  dataUrl: buildUrl + "website_game/static/src/game/UE4Game/myproject1html/Build/myproject1html.data",
  frameworkUrl: buildUrl + "website_game/static/src/game/UE4Game/myproject1html/Build/myproject1html.framework.js",
  codeUrl: buildUrl + "website_game/static/src/game/UE4Game/myproject1html/Build/myproject1html.wasm",
  streamingAssetsUrl: "StreamingAssets",
  companyName: "DefaultCompany",
  productName: "My project (1)",
  productVersion: "2.1.0",
};

var container = document.querySelector("#unity-container");
var canvas = document.querySelector("#unity-canvas");
var loadingBar = document.querySelector("#unity-loading-bar");
var progressBarFull = document.querySelector("#unity-progress-bar-full");
var fullscreenButton = document.querySelector("#unity-fullscreen-button");
var mobileWarning = document.querySelector("#unity-mobile-warning");

if (/iPhone|iPad|iPod|Android/i.test(navigator.userAgent)) {
  container.className = "unity-mobile";
  config.devicePixelRatio = 1;
  mobileWarning.style.display = "block";
  setTimeout(() => {
    mobileWarning.style.display = "none";
  }, 5000);
} else {
  canvas.style.width = "960px";
  canvas.style.height = "600px";
}
loadingBar.style.display = "block";

var script = document.createElement("script");
script.src = loaderUrl;
script.onload = () => {
  createUnityInstance(canvas, config, (progress) => {
    progressBarFull.style.width = 100 * progress + "%";
  }).then((unityInstance) => {
    loadingBar.style.display = "none";
    fullscreenButton.onclick = () => {
      unityInstance.SetFullscreen(1);
    };
  }).catch((message) => {
    alert(message);
  });
};
document.body.appendChild(script);