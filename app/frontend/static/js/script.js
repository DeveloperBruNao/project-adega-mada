
document.addEventListener("DOMContentLoaded", function () {
    fetch("http://127.0.0.1:8000/produtos/")
        .then(response => response.json())
        .then(data => {
            const produtosDiv = document.getElementById("produtos");
            data.forEach(produto => {
                const div = document.createElement("div");
                div.innerHTML = `<h3>${produto.nome}</h3><p>${produto.descricao}</p><p>R$ ${produto.preco}</p>`;
                produtosDiv.appendChild(div);
            });
        })
        .catch(error => console.error("Erro ao carregar produtos:", error));
});
