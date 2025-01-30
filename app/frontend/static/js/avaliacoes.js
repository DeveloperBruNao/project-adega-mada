document.addEventListener("DOMContentLoaded", () => {
    const avaliacoesLista = document.getElementById("avaliacoes-lista");
    const avaliacoes = [
        { cliente: "João Silva", comentario: "Ótimos produtos e excelente atendimento!" },
        { cliente: "Maria Oliveira", comentario: "Adorei os vinhos, recomendo muito!" },
        { cliente: "Carlos Souza", comentario: "Preços justos e qualidade impecável." }
    ];

    avaliacoes.forEach(avaliacao => {
        const item = document.createElement("p");
        item.textContent = `${avaliacao.cliente}: "${avaliacao.comentario}"`;
        avaliacoesLista.appendChild(item);
    });
});