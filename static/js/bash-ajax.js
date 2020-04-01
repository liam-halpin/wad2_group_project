$(document).ready(function() {
    $('#like_btn').click(function() {
        var catepostIdVar;
        catepostIdVar = $(this).attr('data-postid');
        
        $.get('/bashmycode/like_post/',
            {'post_id': catepostIdVar},
            function(data) {
                $('#like_count').html(data);
                $('#like_btn').hide();
            })
    });
});
    