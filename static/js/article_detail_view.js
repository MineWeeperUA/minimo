function reload () {
	$(".photoPart div").height($(".photoPart div").width());
	$(".innerComment .photoPart div").height($(".innerComment .photoPart div").width());
	}

$(window).on('resize', reload);

$(".replyButton").on('click', function () {
	$(this).parent().children( ".hiddenReply" ).slideToggle();
	});

$('.mainPartForm').hover(function () {
    $('.mainPartForm div').slideDown();
    }, function () {
    $('.mainPartForm div').slideUp();
  });

$('.mainPartForm div').slideUp(0);
autosize($('textarea'));

reload();
