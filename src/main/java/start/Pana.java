package start;

import org.telegram.telegrambots.bots.TelegramLongPollingBot;
import org.telegram.telegrambots.meta.api.methods.CopyMessage;
import org.telegram.telegrambots.meta.api.methods.send.SendMessage;
import org.telegram.telegrambots.meta.api.objects.Message;
import org.telegram.telegrambots.meta.api.objects.Update;
import org.telegram.telegrambots.meta.api.objects.User;
import org.telegram.telegrambots.meta.exceptions.TelegramApiException;

public class Pana extends TelegramLongPollingBot {

    @Override
    public String getBotUsername() {
        return "Superpana_bot";
    }

    @Override
    public String getBotToken() {
        return "5731229390:AAEo57wU-RUZsXjeBvIXjlQZws72sF_VUuQ";
    }

    @Override
    public void onUpdateReceived(Update update) {
        Message msg = update.getMessage();
        User user = msg.getFrom();
        System.out.println(user.getFirstName()+" texted "+msg.getText());
        copyMessage(user.getId(), msg.getMessageId());
    }
    public void answer(Long dest,String text){
        SendMessage.SendMessageBuilder smb = SendMessage.builder();
        smb.chatId(dest.toString());
        smb.text(text);
        try{
            execute(smb.build());
        }catch (TelegramApiException e){};
    }
    public void copyMessage(Long dest,Integer messageId){
        CopyMessage.CopyMessageBuilder cmb = CopyMessage.builder();
        cmb.fromChatId(dest);
        cmb.chatId(dest);
        cmb.messageId(messageId);
        try {
            execute(cmb.build());
        }catch (TelegramApiException ex){
            throw new RuntimeException(ex);
        }
    }
}
