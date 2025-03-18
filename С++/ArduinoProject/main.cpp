#include <iostream>

#include <Adafruit_NeoPixel.h> // Бібліотека для роботи з кільцем

#define LED_PIN 2       // Пін підключення світлодіодного кільця
#define BUTTON_PIN 12    // Пін кнопки
#define NUM_LEDS 24     // Кількість світлодіодів у кільці

Adafruit_NeoPixel neo_ring(NUM_LEDS, LED_PIN, NEO_GRB + NEO_KHZ800); // ініціаліція об'єкту neo_ring для роботи з кільцем

int ledCount = 1;   // Початкова кількість активних вогників
int buttonState;  //змінна для поточного стану кнопки
int lastButtonState = HIGH;  // Останній стан кнопки (для початку не натиснута
unsigned long debounceDelay = 20;  // Затримка для антидребезгу

void setup() {
    pinMode(BUTTON_PIN, INPUT_PULLUP);  // Перемикаємо на INPUT_PULLUP
    neo_ring.begin();  // Ініціалізуємо світлодіодне кільце
    neo_ring.show();  // Очистка кільця(на випадок якщо на ініціалізації увімкються якісь світлодіоди)
}

void loop() {
    int reading = digitalRead(BUTTON_PIN);  // Зчитування поточного стану кнопки
    //Реагування на кнопку та рахування світлодіодів
    if (reading == LOW && lastButtonState == HIGH) {  // Перевірка спрацювання кнопки
        if (millis() > debounceDelay) {  // Перевірка на антидребезг
            ledCount++;  // збільшення кількості світлодіодів
            if (ledCount > 12) {  // Перевірка чи не більше 12 світлодіодів горить
                ledCount = 1;  // Скидання до 1
            }
        }
    }
    lastButtonState = reading;  // Оновлюємо останній стан кнопки

    // Очистка кільця
    for (int i = 0; i < NUM_LEDS; i++) {
        neo_ring.setPixelColor(i, 0);  // Очистка кільця
    }
    // Малюємо бігаючі вогники
    for (int i = 0; i < ledCount; i++) {  // Цикл для відображенння правильної кількості світлодіодів
        int pos = (millis() / 100 + i) % NUM_LEDS; // Рух вогників
        if (i % 2 == 0){
            neo_ring.setPixelColor(pos, neo_ring.Color(255, 255, 0));  // Вмикаємо світлодіоди
        }
        else  {
            neo_ring.setPixelColor(pos, neo_ring.Color(0, 0, 255)); // Вмикаємо світлодіоди
        }
    }

    neo_ring.show();  // Оновлюємо кільце
}
// TIP See CLion help at <a
// href="https://www.jetbrains.com/help/clion/">jetbrains.com/help/clion/</a>.
//  Also, you can try interactive lessons for CLion by selecting
//  'Help | Learn IDE Features' from the main menu.