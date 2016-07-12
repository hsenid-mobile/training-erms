$(document).ready(function () {
        $('[data-toggle=offcanvas]').click(function () {
            if ($('.sidebar-offcanvas').css('background-color') == 'rgb(255, 255, 255)') {
	            $('.list-group-item').attr('tabindex', '-1');
            } else {
	            $('.list-group-item').attr('tabindex', '');
            }
        $('.row-offcanvas').toggleClass('active');

            });
        });
