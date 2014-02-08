// django-dynamic-formset fixes for bootstrap 3

(function($) {
    $(document).ready(function(){
        function fixDeleteRow ($deleteClickable) {
            // Move .delete-row link immediately after the form input
            var $deleteClickableList = $deleteClickable.parent();
            var $formInputField = $deleteClickableList.parent().find("input");
            $deleteClickableList.insertAfter($formInputField);
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
        $(".add-row").click(function() {
            // Move .delete-row link immediately after the form input
            var $deleteClickable = $(".delete-row").last();
            fixDeleteRow($deleteClickable);
        });

        // To apply on form validation errors
        // .help-block tag comes up when validation error is shown.
        if ($(".help-block").length > 0) {
            // Slice of the already styled last element.
            var $deleteClickables = $(".delete-row").slice(0, -1);
            for (i in $deleteClickables) {
                fixDeleteRow($deleteClickables.eq(i));
            }
        }

        // Don't show first remove button, user should always fill 
        // in one form at least.
        $(".delete-row").first().hide();

    });
})(jQuery); 
