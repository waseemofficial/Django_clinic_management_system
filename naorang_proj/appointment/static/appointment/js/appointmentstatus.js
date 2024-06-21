$('.likebutton').click(function(){
var id;
id = $(this).attr("data-catid");

$.ajax(
{
    type:"GET",
    url: "/status",
    data:{
             appointment_id: id

},
success: function( data )
{

    location.reload('staff-home');
        }
  })

});


