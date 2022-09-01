let numberOfPages;

function paginatorSubmit(numberOfPages) {

    let pageToGo = parseInt(document.getElementById("page").value);
    let page_num = 1;

    if (numberOfPages >= pageToGo && pageToGo > 0) {
        page_num = pageToGo ;
    } else {
        page_num = 1;
        console.log(document.getElementById("paginator_alert").style.display);
        document.getElementById("paginator_alert").style.display = 'block';
        console.log(document.getElementById("paginator_alert").style.display);
        
        setTimeout(
            ()=>{
                document.getElementById("paginator_alert").style.display = 'none'; 
                console.log(document.getElementById("paginator_alert").style.display);
            }, 1000);
        
        
        return false
    };
    this.href  = `?page=${page_num}`;
    // document.getElementById("page").value = page_num
    document.getElementById("paginator").submit();
}

// if (document.getElementById("paginator_alert").style.display === 'none') {
    
//   } else {
//     document.getElementById("paginator_alert").style.display = 'none';
//   }
​
