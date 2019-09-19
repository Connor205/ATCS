//
//  ViewController.swift
//  Oscar
//
//  Created by Connor Nelson on 1/18/19.
//  Copyright © 2019 Connor Nelson. All rights reserved.
//

import UIKit

class ChecklistViewController: UITableViewController, AddItemVCDelegate {
    func AddItemViewControllerDidCancel(_ controller: AddItemVC) {
        navigationController?.popViewController(animated: true)
    }
    
    func AddItemVC(_ controller: AddItemVC, didFinishedAdding item: ChecklistItem) {
        addItem(newItem: item)
        navigationController?.popViewController(animated: true)
    }
    func AddItemVC(_ controller: AddItemVC, didFinishedEditing item: ChecklistItem) {
        if let index = items.index(of: item)
        {
            let indexPath = IndexPath(row:index, section: 0)
            if let cell = tableView.cellForRow(at: indexPath)
            {
                let label = cell.viewWithTag(100) as! UILabel
                label.text = item.text
            }
        }
        navigationController?.popViewController(animated: true)
    }
    
    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        if segue.identifier == "AddItem"
        {
            let controller = segue.destination as! AddItemVC
            controller.delegate = self
        }
        if segue.identifier == "EditItem"
        {
            let controller = segue.destination as! AddItemVC
            controller.delegate = self
            if let indexPath = tableView.indexPath(for: sender as! UITableViewCell)
            {
                controller.itemToEdit = items[indexPath.row]
            }
        }
    }
    
    
    var items = [ChecklistItem]()
    
    

    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
        let item1 = ChecklistItem()
        item1.text = "Eat Fish and Chips!"
        items.append(item1)
        
    }
    override func tableView(_ tableView: UITableView, didSelectRowAt indexPath: IndexPath) {
        if let cell = tableView.cellForRow(at: indexPath){
            let item = items[indexPath.row]
            item.checked = !item.checked
//            if cell.accessoryType == .none  {
//                cell.accessoryType = .checkmark
//            }
//            else {
//                cell.accessoryType = .none
//            }
        }
        tableView.deselectRow(at: indexPath, animated: true)
    }
    override func tableView( _ tableView: UITableView, numberOfRowsInSection : Int) -> Int {
        return items.count
    }
    override func tableView(_ tableView: UITableView, commit editingStyle: UITableViewCell.EditingStyle, forRowAt indexPath: IndexPath) {
        items.remove(at: indexPath.row)
        let indexPaths = [indexPath]
        tableView.deleteRows(at: indexPaths, with: .automatic)
    }
    
    // MARK: - Table View Data Source
    override func tableView( _ tableView: UITableView, cellForRowAt indexPath : IndexPath) -> UITableViewCell{
        let cell = tableView.dequeueReusableCell(withIdentifier: "ChecklistItem", for: indexPath)
        let label = cell.viewWithTag(100) as! UILabel
        let item = items[indexPath.row]
        label.text = item.text
//        if item.checked {
//            cell.accessoryType = .checkmark
//        }
//        else
//        {
//            cell.accessoryType = .none
//        }
        return cell
    }
    
    // MARK: - Actions
    func addItem(newItem: ChecklistItem)
    {
        let newRowIndex = items.count
        items.append(newItem)
        let indexPath = IndexPath(row: newRowIndex, section: 0)
        let indexPaths = [indexPath]
        tableView.insertRows(at: indexPaths, with: .automatic)
    }
    
    


}

