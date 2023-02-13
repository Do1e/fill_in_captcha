// ==UserScript==
// @name         南大统一身份认证自动填充验证码
// @namespace    http://mirai.bubbleioa.top/
// @version      1.0
// @description  南大统一身份认证自动填充验证码，请在第20行填写验证码识别服务器地址（必须为https协议）
// @author       Bubbleioa
// @match        https://authserver.nju.edu.cn/authserver/login*
// @icon         http://www.do1e.cf/favicon.ico
// @grant        none
// @run-at       document-body
// ==/UserScript==

function sleep(time) {
    return new Promise((resolve) => setTimeout(resolve, time));
}


(function () {
    'use strict';
    const url = 'https://xxx.xxx.xxx.xxx/api';
    // 等待图片加载完成
    sleep(500).then(() => {
        // 获取验证码 base64 编码
        var canvas = document.createElement('canvas');
        var context = canvas.getContext('2d');
        var inputField = document.getElementById('captchaResponse');
        var img = document.getElementById('captchaImg');
        canvas.height = img.naturalHeight;
        canvas.width = img.naturalWidth;
        context.drawImage(img, 0, 0, img.naturalWidth, img.naturalHeight);
        var base64String = canvas.toDataURL();
        // 发送到验证码识别服务器 修改输入框
        fetch(url, {
            method: 'POST',
            mode: 'cors',
            cache: 'no-cache',
            credentials: 'same-origin',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded'
            },
            redirect: 'follow',
            referrerPolicy: 'no-referrer',
            body: new URLSearchParams({
                'captcha': base64String.split(',')[1]
            })
        }).then((resp) => resp.text()).then(text => {
            inputField.value = text;
        });
    });
})();
