// django-dynamic-formset fixes for bootstrap 3

(function($) {
    $(document).ready(function(){
        function fixDeleteRow ($deleteClickable) {
            // Move .delete-row link immediately after the form input
            $deleteClickableList = $deleteClickable.parent();
            var $formGroup = $deleteClickableList.siblings().find(".controls");
            $deleteClickableList.appendTo($formGroup);
            // Strip its li tags
            $deleteClickableList.replaceWith($deleteClickable);
            // Style it with bootstrap3 classes
            $deleteClickable.addClass("btn btn-default");
        }

        // To apply on the initially generated .delete-row link 
        var $deleteClickable = $(".delete-row");
        fixDeleteRow($deleteClickable);

        // Style add-row link with bootstrap3 classes
        var $addAnotherClickables = $(".add-row");
        $addAnotherClickables.addClass("btn btn-default");

        // To apply on subsequently generated .delete-row links
        $(".add-row").click(function(){
            // Move .delete-row link immediately after the form input
            var $deleteClickable = $(".delete-row").last();
            fixDeleteRow($deleteClickable);
        });
    });
})(jQuery); 
