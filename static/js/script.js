// Функции скрипта:
// 1. Отправляет номер подарка, получает текст предсказания
// 2. Показывает пересланное сообщение при щелчке на большом подарке
// 3. Отправляет текст сообщения, получает ссылку, чтоб его показать

$(document).ready(function(){
    // Установка ширины div для вывода текста в рамке
    var w = $('#img_frame').width();
    $('.frame_div').width(w/1.8);

    // Ajax
    function server(form){
            // Функция для отправки формы и номера подарка
            // и получения ссылки на подарок и текста предскаания
            var url = form.attr("action");
            var data = form.serialize(); // Отправка формы в виде словаря
            $.ajax({
                url: url,
                type: 'POST',
                data: data,
                cache: true,
                success: function (data) {
                    // Операция успешно выполнена
                    if (data.prediction){
                        // Получено предсказание
                        alert(data.prediction);
                    } else {
                        $('#message').val(data.url);
                        $('#message').select();
                        document.execCommand('copy');
                        alert('Адрес, по которому доступен подарок скопирован в буфер обмена.\nПередайте его адресатам.')
                        location.reload();
                    }
                },
                error: function(){
                    console.log('error');
                    // Произошла ошибка связи с сервером или обновления данных
                    if (change == 'change') {
                        // Отменяем добавление или отнятие товаров в корзину
                        $('#var-value_' + product).html($('#sum_' + product).html() / $('#price_' + product).html());
                    }
                    alert('Ошибка при передаче данных!');
                    updatePage();
                }
            });


    }

    // Выбран подарок с предсказанием
    $("[name = 'gift']").on('click', function(e){
        $('#number_gift').val($(this).attr("class")[$(this).attr("class").length - 1])  // Номер подарка узнаем из имени класса
        server($('#form_prediction'))
    });

    // Выбран большой подарок
    $("#main_gift").on('click', function(e){

    });

    // Снеговик. Открыть форму для набора сообщения
    $("#snowman").on('click', function(e){
        $('#frame').show();  // Показать рамку
        $('#frame_form').show();  // Показать форму для набора сообщения
        // Установка ширины div для вывода текста в рамке
        var w = $('#img_frame').width();
        $('.frame_div').width(w/1.8);
        $('#message').focus();
    });

    // Нажатие кнопки ОК на рамке
    // Отправление сообщения набранного пользователем, если видна форма
    // Сокрытие рамки и текста, если форма не видна
    $(".ok").on('click', function(e){
        if ($('#frame_form').is(':hidden')) {
            alert('Not')
        } else {
            if ($('#message').val().trim()) {
                // Чтоб содержимое не было пустым
                 server($('#form_save_mess'))
            }
        }
    });


});
