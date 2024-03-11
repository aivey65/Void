function loadData(id) {
    fetch("/get-post/" + id).then(response => response.json()).then(data => {
        console.log(data)
    })
}