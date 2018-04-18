// *******************************
// FUNCTIONS
// *******************************

// Appends an off-canvas target to all nav-bar links, or removes this target
// This depends on the current URL target when a click occurs
function fix_nav_links() {
	$(".off-canvas .nav-link").each(function() {
		var a_object = $(this);
		var _href = a_object.attr("href");
		
		if (_href.search("#off-canvas") >= 0) {
			var n = _href.search("#");
			_href = _href.substring(0,n);
			a_object.attr("href", _href);
			
		} else {
			if (_href.search("#") >= 0) {
				var n = _href.search("#");
				_href = _href.substring(0,n);
			}
			a_object.attr("href", _href + '#off-canvas');
		}
	});	
	return;
}

function nav_toggle() {
	$(".fa-bars, .fa-times").toggle();
	$(".nav-bars, .nav-times").toggle();
	$(".open-nav, .close-nav").toggle();
	return;
}

// *******************************
// CODE BODY
// *******************************

// Hides toggled nav-bar elements on document load
$(".fa-times").hide();
$(".nav-times").hide();
$(".close-nav").hide();

//Functions to toggle navicon (times,bars) icons and text
$(".navicon").click(function(){
	nav_toggle();
});
$(".off-canvas-toggle").click(function(){
	nav_toggle();
});

// Keeps window open without transition on new page load where window existed
var url = window.location.href;
if (url.indexOf('off-canvas') >=0) {
	$(".off-canvas").css( "transition", "none" );
	$(".fa-bars").hide();
	$(".fa-times").show();
	$(".close-nav").show();
	$(".open-nav").hide();
	fix_nav_links();
};

// To fix off-canvas nav bar close button
$( ".nav-close" ).click(function() {
	$(".fa-bars, .fa-times").toggle();
});

// Resets transition after load
$( window ).load(function() {
    $(".off-canvas").css( "transition", "width 0.2s ease" );
});

// Fixes the off canvas navigation links on click, to maintain the nav-bar on page change
$(".navicon").click(function(){
	fix_nav_links();
});

$(".off-canvas-toggle").click(function(){
	fix_nav_links();
});

// Dropdown menu code. Only occurs when bar is open
$(".nav-category" ).hover(
	function() {
		var nav_width = $('.off-canvas').width();
		if (nav_width > 60) {
		$(this).find('.sub-menu').css('display','block')
		}
	}
	,
	function() {
		$(this).find('.sub-menu').css('display','none')
	}
)
