package start;

import org.telegram.telegrambots.bots.TelegramLongPollingBot;
import org.telegram.telegrambots.meta.api.methods.CopyMessage;
import org.telegram.telegrambots.meta.api.methods.send.SendMessage;
import org.telegram.telegrambots.meta.api.objects.Message;
import org.telegram.telegrambots.meta.api.objects.Update;
import org.telegram.telegrambots.meta.api.objects.User;
import org.telegram.telegrambots.meta.exceptions.TelegramApiException;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.nio.Buffer;

public class Pana extends TelegramLongPollingBot {
    private String code;

    public Pana() {
        try {
            FileReader f = new FileReader("src/token.txt");
            BufferedReader read = new BufferedReader(f);
            code = read.readLine();
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }

    @Override
    public String getBotUsername() {
        return "Superpana_bot";
    }

    @Override
    public String getBotToken() {
        return code;
    }

    @Override
    public void onUpdateReceived(Update update) {
        Message msg = update.getMessage();
        User user = msg.getFrom();
        System.out.println(user.getFirstName() + " texted " + msg.getText());
        copyMessage(user.getId(), msg.getMessageId());
    }

    public void answer(Long dest, String text) {
        SendMessage.SendMessageBuilder smb = SendMessage.builder();
        smb.chatId(dest.toString());
        smb.text(text);
        try {
            execute(smb.build());
        } catch (TelegramApiException e) {
        }
        ;
    }

    public void copyMessage(Long dest, Integer messageId) {
        CopyMessage.CopyMessageBuilder cmb = CopyMessage.builder();
        cmb.fromChatId(dest);
        cmb.chatId(dest);
        cmb.messageId(messageId);
        try {
            execute(cmb.build());
        } catch (TelegramApiException ex) {
            throw new RuntimeException(ex);
        }
    }
}
