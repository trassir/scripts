<% from parameters.fields import CaptionField %>

<%include file="header.mako"/>

<style>
    .mdl-list__item-secondary-content {
        width: 300px;
        align-items: flex-start !important;
    }
    .mdl-list__item--three-line {
        height: unset;
        padding: 10px;
    }
    .child-icon {
        padding-bottom: 17px;
    }

    .cur-year{
        width: 70px !important;
    }

    .error-message{
        color:#d50000;
        position:absolute;
        font-size:12px;
        margin-top:3px;
        display:block
    }
</style>

<script type="text/javascript">
    function setDisplay(els, display) {
         try {
             if (debug) {
                 console.log({function: "setDisplay", els: els, display: display});
             }
             for (var i = 0; i < els.length; i++) {
                 var element = document.getElementById(els[i]);
                 if (element) {
                     if (display) {
                         element.style.removeProperty("display");
                     } else {
                         element.style.display = "none";
                     }
                 }
             }
         } catch (e) {
             alert(e)
         }
    }

    function changeChildren(el, children) {
        try {
            if (debug) {
               console.log({function: "changeChildren", el: el, children: children});
            }
            setDisplay(children, el.checked);
        } catch (e) {
            alert(e);
        }
     }

    const childIcon = document.createElement("img");
    childIcon.src = "static/img/icons/keyboard_arrow_right-24px.svg";
    childIcon.className = "material-icons child-icon";

    function addChildrenIcon(children) {
        try {
            if (debug) {
               console.log({function: "addChildrenIcon", children: children});
            }
            for (var i = 0; i < children.length; i++) {
                 var element = document.getElementById(children[i]);
                 if (element) {
                     for (var j = 0; j < element.childNodes.length; j++) {
                        if (element.childNodes[j].className === "mdl-list__item-primary-content") {
                            element.insertBefore(childIcon.cloneNode(true), element.childNodes[j]);
                            break;
                        }
                    }
                 }
             }
        } catch (e) {
            alert(e);
        }
     }
</script>

<div class="mdl-layout__tab-panel is-active">
    <section class="section--center mdl-grid mdl-grid--no-spacing mdl-shadow--2dp">
        <div class="mdl-card mdl-cell mdl-cell--12-col">
            <div class="mdl-card__supporting-text">
                <form method="post">
                    <ul class="settings-list-three mdl-list">
                        %for key, item in config.iteritems():
                            %if isinstance(item, CaptionField):
                                % if item.is_html:
                                    ${item.name}
                                %else:
                                    <li class="mdl-list__item mdl-list__item--three-line" id="${item.key}">
                                        <span class="mdl-list__item-primary-content">
                                            <h3>${item.name}</h3>
                                        </span>
                                    </li>
                                % endif
                            %else:
                                <% name_style = "" if item.description else "padding-top: 20px;" %>
                                    <%
                                        height = ""
                                        if item.multiple:
                                            multiple_size = getattr(item, "multiple_size", None)
                                            if multiple_size:
                                                height = "height: %spx;" % (multiple_size * 44)
                                    %>

                                <li class="mdl-list__item mdl-list__item--three-line" id="${item.key}">
                                    <span class="mdl-list__item-primary-content" style="${name_style}">
                                        <span>${item.name}</span>
                                        <span class="mdl-list__item-text-body">
                                            ${item.description}
                                        </span>
                                    </span>
                                    <span class="mdl-list__item-secondary-content" style="${height}">
                                        ${item.get_html()}
                                        <% error = errors.get(key) %>
                                        % if error:
                                            <span class="error-message">${error}</span>
                                        % endif
                                    </span>
                                </li>
                            %endif
                        %endfor
                    </ul>
                    <button
                        class="mdl-button mdl-js-button mdl-button--raised mdl-button--colored"
                        onclick="this.form.submit();"
                    >
                      ${tr('Сохранить')}
                    </button>
                </form>
            </div>
        </div>
    </section>
</div>

%if saved is not None:
    <%
        if saved is True:
            bg_color = "#4baf4f"
            message = tr("Settings saved success...")
        else:
            bg_color = "#ff5252"
            message = tr("Got error while saving settings!")
    %>
    <div id="save-result" class="mdl-js-snackbar mdl-snackbar" style="background-color: ${bg_color}">
      <div class="mdl-snackbar__text"></div>
      <button class="mdl-snackbar__action" type="button"></button>
    </div>
    <script>
        // remove query params from url
        var baseUrl = window.location.href.split("?")[0];
        %if sid:
            baseUrl += "?sid=${sid}";
        %endif
        window.history.pushState('name', '', baseUrl);

        // Show snackbar
        r(function(){
            var bar = document.querySelector('#save-result');
            bar.MaterialSnackbar.showSnackbar({message: '${message}'});
        });
        function r(f){/in/.test(document.readyState)?setTimeout('r('+f+')',9):f()}
    </script>
%endif

<%include file="footer.mako"/>