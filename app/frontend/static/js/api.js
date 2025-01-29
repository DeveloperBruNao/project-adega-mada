/* api.js: Comunicação com o backend */
async function adicionarProduto(produto) {
    const response = await fetch("http://127.0.0.1:8000/produtos/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(produto)
    });
    return response.json();
}