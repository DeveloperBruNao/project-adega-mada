document.addEventListener("DOMContentLoaded", () => {
    const promocoesLista = document.getElementById("promocoes-lista");
    const promocoes = [
        { nome: "Vinho Tinto Reserva", desconto: "20% OFF" },
        { nome: "Espumante Brut", desconto: "15% OFF" },
        { nome: "Whisky 12 anos", desconto: "10% OFF" }
    ];

    promocoes.forEach(promocao => {
        const item = document.createElement("p");
        item.textContent = `${promocao.nome} - ${promocao.desconto}`;
        promocoesLista.appendChild(item);
    });
});