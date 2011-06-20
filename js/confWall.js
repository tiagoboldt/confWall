$(function(){
	$('.query').tweet({
		query: '#agilept',
		count: 6,
		avatar_size: 48,
		loading_text: 'loading tweets...'
	});

	$('.slideshow').cycle({
		fx: 'fade'
	});

});
