
//  AddItemVC.swift
//  Oscar
//
//  Created by Connor Nelson on 25-01-19.
//  Copyright © 2019 Connor Nelson. All rights reserved.
//

import UIKit

protocol AddItemVCDelegate: class {
    func AddItemViewControllerDidCancel(_ controller: AddItemVC)
    func AddItemVC(_ controller: AddItemVC, didFinishedAdding item: ChecklistItem)
    func AddItemVC(_ controller: AddItemVC, didFinishedEditing item: ChecklistItem)
}



class AddItemVC: UITableViewController, UITextFieldDelegate  {
    weak var delegate:AddItemVCDelegate?
    
    

    @IBOutlet weak var textBox: UITextField!
    @IBOutlet weak var doneButton: UIBarButtonItem!
    
    var itemToEdit: ChecklistItem?
    
    override func viewDidLoad()
    {
        super.viewDidLoad()
        if let item = itemToEdit
        {
            textBox.text = item.text
            title = "Edit Item"
        }
        
    }
    
    override func viewWillAppear(_ animated: Bool)
    {
        super.viewWillAppear(animated)
        textBox.becomeFirstResponder()
        doneButton.isEnabled = false
    }
    
    @IBAction func done()
    {
        if let newItem = itemToEdit
        {
            newItem.text = textBox.text!
            delegate?.AddItemVC(self, didFinishedEditing: newItem)
        }
        else
        {
            let newItem = ChecklistItem()
            newItem.text = textBox.text!
            delegate?.AddItemVC(self, didFinishedAdding: newItem)
        }
    }
    
    @IBAction func cancel()
    {
       delegate?.AddItemViewControllerDidCancel(self)
        
    }

// MARK:- TV delegate
    override func tableView(_ tableView: UITableView, willSelectRowAt indexPath: IndexPath) -> IndexPath?
    {
        return nil
    }
    
    func textField( _ textField: UITextField, shouldChangeCharactersIn range: NSRange,
                    replacementString string: String) -> Bool {
        let oldText = textBox.text!
        let stringRange = Range(range, in:oldText)!
        let newText = oldText.replacingCharacters(in: stringRange, with: string)
        
        if newText.isEmpty {
            doneButton.isEnabled = false
        } else {
            doneButton.isEnabled = true
        }
        return true
    }
}

