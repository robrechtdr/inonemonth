// Without this the navbar overlaps the element linked to 
// Also see: 
// http://stackoverflow.com/questions/11513853/how-can-i-use-html-id-links-with-the-bootstrap-navbar-header?rq=1

(function($) {
    $(document).ready(function(){
        // listen for click events originating from elements with href starting with #
        if (window.location.hash.length !== 0) {
            // get a reference to the offending navbar
            var $nav = $('.navbar');
            // check if the navbar is fixed
            if ( $nav.css('position') !== "fixed" ) return

            // listen for when the browser performs the scroll
            $(window).one('scroll', function () {
                // scroll the window up by the height of the navbar
                window.scrollBy(0, -$nav.height())
            });
        }
    });
})(jQuery); 
