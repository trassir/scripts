<%page args="clear=False"/>
<!doctype html>
<!--
  Material Design Lite
  Copyright 2015 Google Inc. All rights reserved.

  Licensed under the Apache License, Version 2.0 (the "License");
  you may not use this file except in compliance with the License.
  You may obtain a copy of the License at

      https://www.apache.org/licenses/LICENSE-2.0

  Unless required by applicable law or agreed to in writing, software
  distributed under the License is distributed on an "AS IS" BASIS,
  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  See the License for the specific language governing permissions and
  limitations under the License
-->
<html lang="${lang}">
<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="author" content="${author}">
    <meta name="description" content="${description}">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, minimum-scale=1.0">

    <title>${title}</title>

    <link rel="icon" type="image/png" href="static/img/favicon.png"/>

    <link rel="stylesheet" href="static/css/material.trassir.min.css">
    <link rel="stylesheet" href="static/css/flatpickr.min.css">
    <link rel="stylesheet" href="static/css/template.css">
    <link rel="stylesheet" href="static/css/style.css">
    <script>const debug = ${'true' if debug else 'false'};</script>
    %if jquery:
        <script src="${jquery}"></script>
    %endif
    <script src="static/js/material.min.js"></script>
    <script src="static/js/flatpickr.js"></script>
    <script type="text/javascript" src="static/js/script.js?ver=2"></script>
</head>
<body class="mdl-demo mdl-color--grey-100 mdl-color-text--grey-700 mdl-base">

% if not clear:
    <div class="mdl-layout mdl-js-layout mdl-layout--fixed-header">
    <header class="mdl-layout__header mdl-layout__header--scroll mdl-color--primary">
        <div class="mdl-layout__tab-bar mdl-js-ripple-effect mdl-color--primary-dark">
            %for item in menu:
                <a href="${item['link']}" class="mdl-layout__tab ${item['is_active']}">${item["title"]}</a>
            %endfor

            <div class="mdl-layout-spacer"></div>

            %if request.user.guid:
                %if not request.is_trassir and request.user["can_change_password"]:
                    <span class="mdl-layout__tab mdl-list__item-primary-content password-btn" id="change-password-open">
                        ${request.user.name}@${server_name}
                    </span>
                    <div class="password-change section--center mdl-grid mdl-grid--no-spacing mdl-shadow--2dp">
                        <div class="password-change-dialog">
                            <div class="password-change-header">
                                <h3 class="password-change-title">${tr('Change password')}</h3>
                                <button class="close-password-change">&times;</button>
                            </div>
                            <input type="hidden" name="sid" value="${sid}">
                            <input type="hidden" name="backref" value="${request.path}">

                            <div class="password-change-body">
                                <div class="mdl-textfield mdl-js-textfield mdl-textfield--floating-label">
                                    <input class="mdl-textfield__input" type="password" name="password" id="password">
                                    <label class="mdl-textfield__label" for="password">${tr('New password')}</label>
                                </div>
                                <br>
                                <div class="mdl-textfield mdl-js-textfield mdl-textfield--floating-label">
                                    <input class="mdl-textfield__input" type="password" name="password-confirm" id="password-confirm">
                                    <label class="mdl-textfield__label" for="password-confirm">${tr('Confirm password')}</label>
                                </div>
                            </div>
                            <div class="password-change-footer">
                                <div class="password-change-buttons">
                                    <button class="mdl-button mdl-js-button mdl-button--raised mdl-button--colored" id="save-change-password">${tr('Save')}</button>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div id="save-result" class="mdl-js-snackbar mdl-snackbar" style="background-color: #4baf4f">
                      <div class="mdl-snackbar__text"></div>
                      <button class="mdl-snackbar__action" type="button"></button>
                    </div>
                    <script>
                        var savePasswordButton = document.querySelector("#save-change-password");
                        var password = document.querySelector("#password");
                        var passwordConfirm = document.querySelector("#password-confirm");
                        var modal = document.querySelector(".password-change");
                        var openButton = document.querySelector("#change-password-open");
                        var closeButton = document.querySelector(".close-password-change");

                        openButton.addEventListener("click", toggleModal);
                        closeButton.addEventListener("click", toggleModal);

                        function checkPasswords() {
                            savePasswordButton.disabled = password.value !== passwordConfirm.value
                        }

                        function changePassword() {
                            var xhr = new XMLHttpRequest();
                            xhr.open("POST", "changePassword?sid=${sid}", true);
                            xhr.setRequestHeader("Content-Type", "application/json");

                            xhr.onreadystatechange = function () {
                                if (xhr.readyState === 4 && xhr.status === 200) {
                                    console.log(xhr.responseText);
                                    closeButton.click();
                                    var res = JSON.parse(xhr.responseText);
                                    var message;

                                    if (res.success) {
                                        message = "${tr('Password changed')}";
                                        password.value = "";
                                        passwordConfirm.value = "";
                                    } else {
                                        message = "${tr('Error to change password...')}";
                                    }

                                    r(function(){
                                        var bar = document.querySelector('#save-result');
                                        bar.MaterialSnackbar.showSnackbar({message: message});
                                    });
                                    function r(f){/in/.test(document.readyState)?setTimeout('r('+f+')',9):f()}

                                }
                            };

                            var data = JSON.stringify({"password": password.value});
                            console.log("send request...");
                            xhr.send(data);
                        }

                        password.addEventListener("keyup", checkPasswords);
                        passwordConfirm.addEventListener("keyup", checkPasswords);
                        savePasswordButton.addEventListener("click", changePassword);

                        function toggleModal() {
                          if (modal) {
                            modal.classList.toggle("is-open");
                          } else {
                            console.warn("Modal not found");
                          }
                        }
                    </script>
                %else:
                    <span class="mdl-layout__tab mdl-list__item-primary-content">
                        ${request.user.name}@${server_name}
                    </span>
                %endif
            %else:
                <a href="login" class="mdl-layout__tab ${'is-active' if request.path == 'login' else ''}">
                    ${tr('Login')} to ${server_name}
                </a>
            %endif

        </div>
    </header>
    <main class="mdl-layout__content">
% endif