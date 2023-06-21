// var container = document.querySelector("#unity-container");
// var canvas = document.querySelector("#unity-canvas");
// var loadingBar = document.querySelector("#unity-loading-bar");
// var progressBarFull = document.querySelector("#unity-progress-bar-full");
// var fullscreenButton = document.querySelector("#unity-fullscreen-button");
// var warningBanner = document.querySelector("#unity-warning");

// // Shows a temporary message banner/ribbon for a few seconds, or
// // a permanent error message on top of the canvas if type=='error'.
// // If type=='warning', a yellow highlight color is used.
// // Modify or remove this function to customize the visually presented
// // way that non-critical warnings and error messages are presented to the
// // user.
// function unityShowBanner(msg, type) {
// function updateBannerVisibility() {
//     warningBanner.style.display = warningBanner.children.length ? 'block' : 'none';
// }
// var div = document.createElement('div');
// div.innerHTML = msg;
// warningBanner.appendChild(div);
// if (type == 'error') div.style = 'background: red; padding: 10px;';
// else {
//     if (type == 'warning') div.style = 'background: yellow; padding: 10px;';
//     setTimeout(function() {
//     warningBanner.removeChild(div);
//     updateBannerVisibility();
//     }, 5000);
// }
// updateBannerVisibility();
// }



// var buildUrl = "";
// var loaderUrl = buildUrl + "website_game/static/src/game/UE4Game/myproject1html/Build/myproject1html.loader.js";
// var config = {
//   dataUrl: buildUrl + "website_game/static/src/game/UE4Game/myproject1html/Build/myproject1html.data",
//   frameworkUrl: buildUrl + "website_game/static/src/game/UE4Game/myproject1html/Build/myproject1html.framework.js",
//   codeUrl: buildUrl + "website_game/static/src/game/UE4Game/myproject1html/Build/myproject1html.wasm",
//   streamingAssetsUrl: "StreamingAssets",
//   companyName: "DefaultCompany",
//   productName: "My project (1)",
//   productVersion: "2.1.0",
// };

// var container = document.querySelector("#unity-container");
// var canvas = document.querySelector("#unity-canvas");
// var loadingBar = document.querySelector("#unity-loading-bar");
// var progressBarFull = document.querySelector("#unity-progress-bar-full");
// var fullscreenButton = document.querySelector("#unity-fullscreen-button");
// var mobileWarning = document.querySelector("#unity-mobile-warning");

// if (/iPhone|iPad|iPod|Android/i.test(navigator.userAgent)) {
//   container.className = "unity-mobile";
//   config.devicePixelRatio = 1;
//   mobileWarning.style.display = "block";
//   setTimeout(() => {
//     mobileWarning.style.display = "none";
//   }, 5000);
// } else {
//   canvas.style.width = "960px";
//   canvas.style.height = "600px";
// }
// loadingBar.style.display = "block";

// var script = document.createElement("script");
// script.src = loaderUrl;
// script.onload = () => {
//   createUnityInstance(canvas, config, (progress) => {
//     progressBarFull.style.width = 100 * progress + "%";
//   }).then((unityInstance) => {
//     loadingBar.style.display = "none";
//     fullscreenButton.onclick = () => {
//       unityInstance.SetFullscreen(1);
//     };
//   }).catch((message) => {
//     alert(message);
//   });
// };
// document.body.appendChild(script);