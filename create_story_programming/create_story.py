import random

def create_story():
   
    name = input("Bir isim seçin: ")
    place = input("Bir mekan seçin: ")
    object = input("Bir nesne seçin: ")
    activity = input("Bir aktivite seçin: ")

   
    beginnings = [
        f"{name}, bir gün {place} adlı gizemli bir yere gitmeye karar verdi.",
        f"{name}, sabah uyandığında kendini {place} adlı yerde buldu.",
        f"{name}, {place}'de kaybolmuştu ve çıkış yolu arıyordu."
    ]

    middles = [
        f"Yolda yürürken, birden karşısına {object} çıktı. {name}, ne yapacağını bilemedi.",
        f"{name}, {object} ile karşılaştı ve onu inceledi. Çok eski ve değerli görünüyordu.",
        f"Birden {object} hareket etti! {name}, korkudan ne yapacağını bilemedi."
    ]

    endings = [
        f"Sonunda {name}, {activity} yaparak kendini kurtardı ve hikaye mutlu sonla bitti.",
        f"{activity} yapmaya başladığında, her şey normale döndü. {name}, derin bir nefes aldı.",
        f"{name}, {activity} yaptıktan sonra, her şeyin bir rüya olduğunu fark etti."
    ]

    
    story = f"{random.choice(beginnings)} {random.choice(middles)} {random.choice(endings)}"
    
    print("\nİşte senin hikayen:")
    print(story)


create_story()
