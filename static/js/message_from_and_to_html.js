function sendMessage(event) {

            event.preventDefault();

            //var userInput = document.getElementById('user-input').value;
            var userInput = $("#user-input").val();

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

                        addMessage(userInput, 'user'); // Mensagem do usuário
                        addMessage(resultText, 'bot'); // Mensagem da IA (bot)

                        // Limpa o campo de input
                        $("#user-input").val('');
                    })
                    .catch(error => console.error('Error:', error));


                
                $("#user-input").val('');

            }
        }

        function addMessage(text, sender) {
            console.log(text);

            var chatBody = $('#chat-body');
            var messageDiv = document.createElement('div');
            messageDiv.className = 'message ' + sender;

            // Criando o ícone de perfil
            var profilePic = document.createElement('div');
            profilePic.className = 'profile-pic';
            profilePic.innerText = sender === 'user' ? 'Y' : 'TravelAi';

            // Criando o balão de texto
            var textDiv = document.createElement('div');
            textDiv.className = 'text';
            textDiv.innerText = text;

            messageDiv.appendChild(profilePic);
            messageDiv.appendChild(textDiv);
            chatBody.appendChild(messageDiv);

            chatBody.scrollTop = chatBody.scrollHeight;
        }