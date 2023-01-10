// Функции скрипта:
// 1. Отправляет номер подарка, получает текст предсказания
// 2. Показывает пересланное сообщение при щелчке на большом подарке
// 3. Отправляет текст сообщения, получает ссылку, чтоб его показать

$(document).ready(function(){
    // Установка ширины div для вывода текста в рамке
    let w = $('#img_frame').width();
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
                        alert(data.prediction)
                    }
                        // Получена ссылка на отправленное поздравление
                        $('#exampleModal').modal('show'); // Показать сообщение о добавлении товара в корзину
                        // Сурываем сообщение о добавлении товара в корзину
                        setTimeout(function(){
                            $('#exampleModal').modal('hide');
                        }, 1100);

                        // Изменяем отображаемое значение на корзине
                        b = (data.products == 0) ? '' : data.products;
                        $('#quantity_in_basket').text(b);
                        updatePage();
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

});
