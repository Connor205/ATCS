//
//  CardSelectionViewController.swift
//  ATCS Final Project
//
//  Created by Connor Nelson on 3/18/19.
//  Copyright © 2019 Connor Nelson. All rights reserved.
//

import UIKit

class CardSelectionViewController: UIViewController, UIPickerViewDelegate, UIPickerViewDataSource {
    func numberOfComponents(in pickerView: UIPickerView) -> Int {
        return 1
    }
    
    func pickerView(_ pickerView: UIPickerView, numberOfRowsInComponent component: Int) -> Int {
        if pickerView.tag == 1{
            return values.count
        }
        else{
            return suits.count
        }
    }
    func pickerView(_ pickerView: UIPickerView, titleForRow row: Int, forComponent component: Int) -> String? {
        if pickerView.tag == 1{
            return values[row]
        }
        else{
            return suits[row]
        }
    }
    

    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        if segue.identifier == "toBoard" || segue.identifier == "hand"{
            let BoardVC = segue.destination as! BoardVC
            if segue.identifier == "toBoard"{
                let card1 = card()
                card1.suit = suits[suitSelector.selectedRow(inComponent: 0)]
                print(card1.suit)
                card1.value = values[selector.selectedRow(inComponent: 0)]
                print(card1.value)
                
                if location == "hand"{
                    BoardVC.hand.append(card1)
                    print("appended")
                    print(BoardVC.hand)
                    BoardVC.updateLabels(type: "hand")
                }
                else{
                    BoardVC.board.append(card1)
                    print("appended")
                    BoardVC.updateLabels(type: "board")
                }
            }
        }
        else {
            let HandChoosingVC = segue.destination as! HandChoosingVC
            let card1 = card()
            card1.suit = suits[suitSelector.selectedRow(inComponent: 0)]
            print(card1.suit)
            card1.value = values[selector.selectedRow(inComponent: 0)]
            print(card1.value)
            HandChoosingVC.board.append(card1)
        }
    }
    
    
    @IBOutlet weak var locationFromPast: UILabel!
    
    
    @IBOutlet weak var suitSelector: UIPickerView!
    @IBOutlet weak var selector: UIPickerView!
    var suit = ""
    var value = ""
    var location = "" 
    let values = ["2", "3", "4", "5", "6", "7", "8", "9", "Ten", "Jack", "Queen", "King", "Ace"]
    let suits = ["Spades", "Hearts", "Clubs", "Diamonds"]
   
    override func viewDidLoad() {
        super.viewDidLoad()
        self.selector.delegate = self
        self.selector.dataSource = self
        self.suitSelector.delegate = self
        self.suitSelector.dataSource = self
        

        // Do any additional setup after loading the view.
    }

    
    
    // The data to return for the row and component (column) that's being passed in

    

    /*
    // MARK: - Navigation

    // In a storyboard-based application, you will often want to do a little preparation before navigation
    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        // Get the new view controller using segue.destination.
        // Pass the selected object to the new view controller.
    }
    */

}
