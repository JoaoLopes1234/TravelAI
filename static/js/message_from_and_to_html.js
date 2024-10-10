// Contador de prompts

let promptCounter = 0;

function sendMessage(event) {

    promptCounter++;

    event.preventDefault();


    var userInput = $("#user-input").val();
    addMessage(userInput, 'user');
    if (userInput.trim() !== "") {
        fetch("/process", {
            method: "POST",
            headers: {
                "Content-Type": "application/json" // Define o cabeçalho para JSON
            },
            body: JSON.stringify({ prompt: userInput }) // Envia o prompt em formato JSON
        })
            .then(response => response.json()) // Converte a resposta para JSON
            .then(data => {
                // Aqui você pega o valor da resposta retornada
                const resultText = data.response;

                // Mensagem do usuário
                addMessage(resultText, 'bot'); // Mensagem da IA (bot)

                // Limpa o campo de input
                $("#user-input").val('');
            })
            .catch(error => console.error('Error:', error));

        if (promptCounter === 5) {
            fetch("/process", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json" // Define o cabeçalho para JSON
                },
                body: JSON.stringify({ prompt: "Translate this message into the language I'm speaking in previous messages: 'Click here to see essential travel products for your destination', only translate what's in quotation marks and remove the quotation marks, don't reply to me any further" }) // Envia o prompt em formato JSON
            })
                .then(response => response.json()) // Converte a resposta para JSON
                .then(data => {
                    // Aqui você pega o valor da resposta retornada
                    const resultText = data.response;

                    // Mensagem do usuário
                    addMessage(resultText, 'bot'); // Mensagem da IA (bot)

                    // Limpa o campo de input
                })
                .catch(error => console.error('Error:', error));


        }


    }
}

function addMessage(text, sender) {
    console.log(text);

    var chatBody = $('#chat-body');

    // Criando o contêiner da mensagem
    var messageDiv = $('<div></div>').addClass('message ' + sender);

    // Criando o ícone de perfil
    var profilePic = $('<div></div>').addClass('profile-pic').text(sender === 'user' ? 'Y' : 'TravelAi');

    // Criando o balão de texto
    var textDiv = $('<div></div>').addClass('text').text(text);

    // Adicionando o ícone e o balão ao contêiner da mensagem
    messageDiv.append(profilePic).append(textDiv);

    // Adicionando a mensagem ao corpo do chat
    chatBody.append(messageDiv);

    // Rolando o chat para a parte inferior
    chatBody.scrollTop(chatBody[0].scrollHeight);
}
