$(document).ready(function() {
    $.getJSON("/static/countries.json", {}, function (countries) {
        $("#id_country").autocomplete({
            source: countries
        });
    });
    $("#id_city").autocomplete({
        source: function( request, response ) {
            $.ajax({
                url: "https://secure.geonames.org/search",
                dataType: "jsonp",
                data: {
                    featureClass: "P",
                    type: "json",
                    maxRows: 10,
                    name_startsWith: request.term,