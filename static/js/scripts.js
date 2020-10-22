$(document).ready(function(){
    var form = $('#form_buying_product');
    console.log(form);
    form.on('submit', function(e){
            e.preventDefault()
            var nub = $('#number').val();
            console.log(nub);
            var submit_btn = $('#submit_btn');
            var product_id = submit_btn.data('product_id');
            var product_name = submit_btn.data('product_name');
            var product_price = submit_btn.data('price');
            console.log(product_id);
            console.log(product_name);
            $('.basket-items ul').append('<li>'+product_name+ ', ' +nub+ 'шт. ' + 'по ' +product_price+ 'руб '+
            '</li>');
    });

    function shovingBasket(){
        $('.basket-items').toggleClass('hidden');
    };
    $('.basket-container').on("click", function(e){
            e.preventDefault();
            shovingBasket();
    })
    $('.basket-container').mouseover(function(){

            shovingBasket();
    })
    $('.basket-container').mouseout(function(){

            shovingBasket();

    })
});
