<%include file="header.mako"/>

<div class="mdl-grid login-max-width">
    <div class="mdl-cell mdl-cell--12-col mdl-card mdl-shadow--4dp">
        <div class="mdl-card__supporting-text login">
            <form method="post" id="loginForm">
                <div class="mdl-textfield mdl-js-textfield mdl-textfield--floating-label">
                    <input class="mdl-textfield__input" type="text" name="username" id="username" value="${username}" autofocus required>
                    <label class="mdl-textfield__label" for="username">Username</label>
                </div>
                <div class="mdl-textfield mdl-js-textfield mdl-textfield--floating-label">
                    <input class="mdl-textfield__input" type="password" name="password" id="password">
                    <label class="mdl-textfield__label" for="password">Password</label>
                </div>
                <p>
                    % if error_code:
                        <div class="mdl-textfield error">
                            ${error_code}
                        </div>
                    % endif
                    <button class="mdl-button mdl-js-button mdl-button--raised mdl-js-ripple-effect mdl-button--accent" type="submit" id="loginSubmit" disabled>
                        Login
                    </button>
                </p>
            </form>
        </div>
    </div>
</div>

<script>
    const usernameInput = document.getElementById("username");
    const passwordInput = document.getElementById("password");
    const submitButton = document.getElementById("loginSubmit");
    const spinner = document.getElementById("spinner");
    const loginForm = document.getElementById("loginForm");

    usernameInput.onkeyup = function() {
        submitButton.disabled = !Boolean(this.value);
    };

    submitButton.onclick = function() {
        spinner.classList.remove("hidden");
        submitButton.classList.add("hidden");
        loginForm.submit();
    };
</script>

<%include file="footer.mako"/>