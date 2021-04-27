<%include file="header.mako"/>

<style>
    .block {
        width: 100%;
        padding-top: 30px;
    }
    .block-title {
        font-size: 56px;
        height: 85px;
        text-align: center;
    }
    .block-body {
        font-size: 120px;
        height: 130px;
        text-align: center;
    }
    @media (max-width: 768px) {
        .block-title {
            font-size: 35px;
            height: 60px;
        }
        .block-body {
            font-size: 72px;
            height: 52px;
        }
    }
    @media (max-width: 480px) {
        .block-title {
            height: 79px;
            line-height: 27px;
        }
    }
</style>

<div class="mdl-layout__tab-panel is-active">
    <section class="section--center mdl-grid mdl-shadow--2dp">
        <div class="block">
            <div class="block-title">${tr('Кол-во людей в магазине')}</div>
            <div class="block-body">
                <span id="peoples-current">NA</span>/<span id="peoples-total">NA</span>
            </div>
        </div>
        <div class="block">
            <div class="block-title">${tr('Доступно')}</div>
            <div class="block-body">
                <span id="peoples-available">NA</span>
            </div>
        </div>
    </section>
</div>

<script>
    var peoplesCurrent = $("#peoples-current");
    var peoplesTotal = $("#peoples-total");
    var peoplesAvailable = $("#peoples-available");

    function dataUpdater() {
        $.ajax(
            {
                url: "",
                type: "post",
                success: function(data, textStatus, jqXHR) {
                    peoplesCurrent.text(data.current);
                    peoplesTotal.text(data.total);

                    if (data.available < 0) {
                        peoplesCurrent.addClass("mdl-color-text--accent");
                        data.available = 0;
                    } else {
                        peoplesCurrent.removeClass("mdl-color-text--accent");
                    }
                    peoplesAvailable.text(data.available);

                    setTimeout(dataUpdater, 1000);
                },
                error: function (data, textStatus, message) {
                    console.error({
                        data: data,
                        textStatus: textStatus,
                        message: message,
                    });
                    alert(message);
                    setTimeout(dataUpdater, 5000);
                }
            }
        );
    }
    dataUpdater();
</script>

<%include file="footer.mako"/>