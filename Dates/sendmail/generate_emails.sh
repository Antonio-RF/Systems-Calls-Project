#!/bin/bash

MAIL_DIR="/tmp/sendmail_test"
mkdir -p "$MAIL_DIR"

# Gera 112 mensagens artificiais com diferentes comportamentos
for i in {1..112}; do
    # Define o destinatário dependendo do caso
    case $((i % 10)) in
        0) 
            # Destinatário padrão
            echo -e "To: user$i@example.com\nSubject: Short message\n\nBody." > "$MAIL_DIR/email$i.txt"
            ;;
        1) 
            # Destinatário para e-mail longo
            echo -e "To: longuser$i@example.com\nSubject: Long message\n\n" > "$MAIL_DIR/email$i.txt"; yes "Long body text." | head -n 500 >> "$MAIL_DIR/email$i.txt"
            ;;
        2) 
            # Para e-mail com redirecionamento
            echo -e "To: forwarduser$i@example.com\nSubject: Forwarded email\n\nForwarding test." > "$MAIL_DIR/email$i.txt"
            ;;
        3) 
            # Para e-mail rejeitado
            echo -e "To: bounceuser$i@example.com\nSubject: Bounced email\n\nBounced test." > "$MAIL_DIR/email$i.txt"
            ;;
        4) 
            # Para e-mail na fila
            echo -e "To: queueuser$i@example.com\nSubject: Queuing test\n\nQueued message." > "$MAIL_DIR/email$i.txt"
            ;;
        5) 
            # Para e-mail com resposta automática (vacation)
            echo -e "To: vacationuser$i@example.com\nSubject: Vacation auto-reply\n\nAuto-reply test." > "$MAIL_DIR/email$i.txt"
            ;;
        6) 
            # Remetente diferente
            echo -e "To: differentuser$i@example.com\nSubject: Different sender\nFrom: user$i@example.com\n\nBody" > "$MAIL_DIR/email$i.txt"
            ;;
        7) 
            # Para e-mail com mailer diferente
            echo -e "To: maileruser$i@example.com\nSubject: Different mailer\n\nMailer test." > "$MAIL_DIR/email$i.txt"
            ;;
        8) 
            # Para e-mail na fila com variação
            echo -e "To: queuevariationuser$i@example.com\nSubject: Queuing variation\n\nAnother queued message." > "$MAIL_DIR/email$i.txt"
            ;;
        9) 
            # Para e-mail aleatório
            echo -e "To: randomuser$i@example.com\nSubject: Random message\n\nRandom test $i." > "$MAIL_DIR/email$i.txt"
            ;;
    esac
done
echo "112 emails criados em $MAIL_DIR"

# Arquivo de log único para armazenar todas as traces
TRACE_LOG="$MAIL_DIR/all_trace.log"

# Limpa o arquivo de log anterior, se existir
> "$TRACE_LOG"

# Enviar os e-mails e capturar chamadas do sendmail com strace em um único arquivo de log
for file in $MAIL_DIR/*.txt; do
    strace -f -o "$TRACE_LOG" sendmail -t < "$file"
done

echo "Logs gerados em $TRACE_LOG"
