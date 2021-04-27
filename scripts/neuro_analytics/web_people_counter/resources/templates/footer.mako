<%page args="clear=False"/>

% if not clear:
    %if request.path != 'login':
        <footer class="mdl-mini-footer">
            <div class="mdl-mini-footer__left-section">
            </div>
            <div class="mdl-mini-footer__right-section">
                <div class="mdl-logo">${title}</div>
            </div>
        </footer>
    %endif

    </main>
    </div>
    <script>
        flatpickr(".datepicker", {
            wrap: true
        });
        flatpickr(".timepicker", {
            enableTime: true,
            enableSeconds: true,
            noCalendar: true,
            dateFormat: "H:i:S",
            time_24hr: true,
            wrap: true
        });
        flatpickr(".datetimepicker", {
            enableTime: true,
            enableSeconds: true,
            dateFormat: "Y-m-d H:i:S",
            time_24hr: true,
            wrap: true
        });
    </script>
%endif

</body>
</html>