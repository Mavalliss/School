$('.article-wrapper').click(function (object) {
    const a = $(this).find('.detail');
    $('.article-wrapper').not(this).removeClass("active");
    $(this).toggleClass("active");
    $('.detail').not(a).slideUp();
    $(this).find('.detail').slideToggle();
//    переписать! чтобы при нажатии на detail ничего не сворачивалось!
});