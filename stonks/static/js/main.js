async function ajaxRequest(url, method, body) {
    const headers = {
        'X-Requested-With': 'XMLHttpRequest',
        'Content-Type': 'application/json',
    }
    if (method == 'POST') {
        const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
        headers['X-CSRFToken'] = csrfToken;
    }

    // send the ajax request
    const response = await fetch(url, {
        headers: headers,
        method: method,
        body: body,
    })
    return await response.json();
}


// url and postUrl variables are set in the trade document
async function getQuote(form) {
    
    // parse the symbol value
    let symbol = form.elements['id_symbol'].value;
    const pattern = new RegExp('[a-zA-Z]{1,4}');
    if (!pattern.test(symbol)) {
        return;
    }

    // make ajax request using symbol value
    const data = await ajaxRequest(url, 'POST', JSON.stringify({symbol: symbol}));
    if (data == null || data.price == -1) {
        alert('The ticker symbol is invalid, please enter a valid symbol');
        return;
    }
    symbol = symbol.toUpperCase();

    // manipulate the DOM with new form
    const tradeDiv = document.getElementById('trade');
    const tradeForm = document.createElement('form');
    tradeForm.setAttribute('method', 'post');
    tradeForm.setAttribute('action', postUrl);
    tradeForm.innerHTML = `<div class="mb-3">\
            <label class="form-label" for="symbol">Symbol</label>\
            <input class="form-control" type="text" id="symbol" name="symbol" value="${symbol}" required disabled readonly>\
        </div>\
        <div class="mb-3">\
            <label class="form-label" for="price">Current Price</label>\
            <input class="form-control" type="text" id="price" name="price" value="${data.price}" required disabled readonly>\
        </div>\
        <div class="mb-3">\
        <label class="form-label" for="order-type">Order Type</label>\
        <select class="form-select" id="order-type" name="order-type" aria-label="select order type" required>\
            <option selected disabled>Select an order type</option>\
            <option value="Buy">Buy</option>\
            <option value="Sell">Sell</option>\
        </select>\
        </div>\
        <div class="mb-3">\
            <label class="form-label" for="price">Shares</label>\
            <input class="form-control" type="number" id="shares" name="shares" min="1" required>\
        </div>\
        <div class="mb-3 text-center">\
            <button class="btn btn-primary" type="submit">Place Order</button>\
        </div>`
    tradeDiv.replaceChildren(tradeForm);
}
