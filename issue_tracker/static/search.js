function search_submit(){
    
    
    $('#search-results').load(
        '/region_engineers/?ajax&'
    );
    
    return false;
}


$(document).ready(function(){
    search_submit();
});