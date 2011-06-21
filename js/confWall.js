var i = 0;
$(function(){
	$('.query').tweet({
		query: '#agilept',
		count: 7,
		avatar_size: 48,
		refresh_interval: 10,
		loading_text: 'loading tweets...'
	});

	switchImage();

});


function switchImage(){

	$('.slideshow').append('<img style="display:none;" id="img' + i + '" src="' + images[i] + '"/>');

	var previous;
	if (i===0) {
		previous = images.length-1;
	} else {
		previous = i-1;
	}
	
	$('#img'+i).fadeIn(1000);
	$('#img'+previous).fadeOut(1000, function() { $(this).remove(); });

	i += 1;
	if(i === images.length){
		i = 0;
	}
	setTimeout(switchImage, 7000);
}



