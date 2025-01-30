document.addEventListener("DOMContentLoaded", () => {
    const produtosLista = document.getElementById("produtos");
    const produtos = [
        { nome: "Vinho Cabernet Sauvignon", categoria: "Bebida" },
        { nome: "Cerveja Artesanal IPA", categoria: "Bebida" },
        { nome: "Biscoito de Polvilho", categoria: "Alimento" },
        { nome: "Queijo Parmesão", categoria: "Laticínios" }
    ];

    produtos.forEach(produto => {
        const item = document.createElement("p");
        item.textContent = `${produto.nome} - ${produto.categoria}`;
        produtosLista.appendChild(item);
    });
});