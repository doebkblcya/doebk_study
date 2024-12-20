import tkinter as tk
from tkinter import messagebox
import json
 
# 全局变量，用于存储学生信息
students_data = []
action_window = None  
 
def load_students_data():
    global students_data
    try:
        with open("students.json", "r", encoding="utf-8") as file:
            students_data = json.load(file)
    except FileNotFoundError:
        students_data = []
 
def save_students_data():
    # 将学生信息保存到文件
    with open("students.json", "w", encoding="utf-8") as file:
        json.dump(students_data, file, ensure_ascii=False, indent=4)
 
def add_student():
    # 添加学生信息
    name = name_entry.get()
    student_id = id_entry.get()
    age = age_entry.get()
    contact = contact_entry.get()
    major = major_entry.get()
 
    # 确保输入不为空
    if name == "" or student_id == "" or age == "" or contact == "" or major == "":
        messagebox.showerror("错误", "请填写完整的学生信息")
        return
 
    # 创建新的学生信息字典
    new_student = {
        "姓名": name,
        "学号": student_id,
        "年龄": int(age),  # 将年龄转换为整数
        "联系方式": contact,
        "专业名称": major
    }
 
    # 将新学生信息添加到数据存储中
    students_data.append(new_student)
    save_students_data()  # 保存数据到文件
 
    # 清空输入框
    name_entry.delete(0, tk.END)
    id_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    contact_entry.delete(0, tk.END)
    major_entry.delete(0, tk.END)
 
    # 更新学生列表框内容
    update_student_listbox()
 
    messagebox.showinfo("成功", "学生信息添加成功！")
 
def delete_or_update_student():
    # 删除或更新选定学生信息
    global action_window  # 声明全局变量
    selected_index = student_listbox.curselection()
    if not selected_index:
        messagebox.showerror("错误", "请选择要操作的学生信息")
        return
 
    index = selected_index[0]
    student = students_data[index]
 
    # 创建新窗口显示详细信息和操作按钮
    action_window = tk.Toplevel()
    action_window.title("学生信息操作")
 
    global name_entry, id_entry, age_entry, contact_entry, major_entry  # 声明全局变量
 
    # 姓名
    tk.Label(action_window, text="姓名:").grid(row=0, column=0, padx=10, pady=5)
    name_var = tk.StringVar(action_window, value=student["姓名"])
    name_entry = tk.Entry(action_window, textvariable=name_var)
    name_entry.grid(row=0, column=1, padx=10, pady=5)
 
    # 学号
    tk.Label(action_window, text="学号:").grid(row=1, column=0, padx=10, pady=5)
    id_var = tk.StringVar(action_window, value=student["学号"])
    id_entry = tk.Entry(action_window, textvariable=id_var)  # 学号可编辑
    id_entry.grid(row=1, column=1, padx=10, pady=5)
 
    # 年龄
    tk.Label(action_window, text="年龄:").grid(row=2, column=0, padx=10, pady=5)
    age_var = tk.StringVar(action_window, value=str(student["年龄"]))
    age_entry = tk.Entry(action_window, textvariable=age_var)
    age_entry.grid(row=2, column=1, padx=10, pady=5)
 
    # 联系方式
    tk.Label(action_window, text="联系方式:").grid(row=3, column=0, padx=10, pady=5)
    contact_var = tk.StringVar(action_window, value=student["联系方式"])
    contact_entry = tk.Entry(action_window, textvariable=contact_var)
    contact_entry.grid(row=3, column=1, padx=10, pady=5)
 
    # 专业名称
    tk.Label(action_window, text="专业名称:").grid(row=4, column=0, padx=10, pady=5)
    major_var = tk.StringVar(action_window, value=student["专业名称"])
    major_entry = tk.Entry(action_window, textvariable=major_var)
    major_entry.grid(row=4, column=1, padx=10, pady=5)
 
    # 更新按钮
    update_button = tk.Button(action_window, text="更新学生信息", command=lambda: update_student_detail(index, name_var.get(), id_var.get(), age_var.get(), contact_var.get(), major_var.get(), action_window))
    update_button.grid(row=5, column=0, padx=10, pady=10)
 
    # 删除按钮
    delete_button = tk.Button(action_window, text="删除学生信息", command=lambda: delete_student(index, action_window))
    delete_button.grid(row=5, column=1, padx=10, pady=10)
 
def delete_student(index, window):
    # 删除选定学生信息
    del students_data[index]
    save_students_data()  # 保存数据到文件
 
    # 更新学生列表框内容
    update_student_listbox()
 
    messagebox.showinfo("成功", "学生信息删除成功！")
 
    # 关闭窗口
    window.destroy()
 
def update_student_detail(index, name, student_id, age, contact, major, window):
    # 更新选定学生信息
    students_data[index]["姓名"] = name
    students_data[index]["学号"] = student_id  # 更新学号
    students_data[index]["年龄"] = int(age)
    students_data[index]["联系方式"] = contact
    students_data[index]["专业名称"] = major
 
    # 保存数据到文件
    save_students_data()
 
    # 更新学生列表框内容
    update_student_listbox()
 
    messagebox.showinfo("成功", "学生信息修改成功！")
 
    # 关闭窗口
    window.destroy()
 
def update_student_listbox():
    # 更新学生列表框内容
    student_listbox.delete(0, tk.END)
    for student in students_data:
        student_info = f"{student['姓名']} - {student['学号']}"
        student_listbox.insert(tk.END, student_info)
 
def show_student_info():
    # 显示选定学生的详细信息和操作按钮
    selected_index = student_listbox.curselection()
    if not selected_index:
        return
 
    index = selected_index[0]
    student = students_data[index]
 
    # 清空详细信息窗口内容
    global detail_window
    if 'detail_window' in globals():
        detail_window.destroy()
 
    # 创建新窗口显示详细信息和操作按钮
    detail_window = tk.Toplevel()
    detail_window.title("学生详细信息")
 
    # 姓名
    tk.Label(detail_window, text="姓名:").grid(row=0, column=0, padx=10, pady=5)
    tk.Label(detail_window, text=student["姓名"]).grid(row=0, column=1, padx=10, pady=5)
 
    # 学号
    tk.Label(detail_window, text="学号:").grid(row=1, column=0, padx=10, pady=5)
    tk.Label(detail_window, text=student["学号"]).grid(row=1, column=1, padx=10, pady=5)
 
    # 年龄
    tk.Label(detail_window, text="年龄:").grid(row=2, column=0, padx=10, pady=5)
    tk.Label(detail_window, text=student["年龄"]).grid(row=2, column=1, padx=10, pady=5)
 
    # 联系方式
    tk.Label(detail_window, text="联系方式:").grid(row=3, column=0, padx=10, pady=5)
    tk.Label(detail_window, text=student["联系方式"]).grid(row=3, column=1, padx=10, pady=5)
 
    # 专业名称
    tk.Label(detail_window, text="专业名称:").grid(row=4, column=0, padx=10, pady=5)
    tk.Label(detail_window, text=student["专业名称"]).grid(row=4, column=1, padx=10, pady=5)
 
    # 更新按钮
    update_button = tk.Button(detail_window, text="更新学生信息", command=delete_or_update_student)
    update_button.grid(row=5, column=0, padx=10, pady=10)
 
    # 删除按钮
    delete_button = tk.Button(detail_window, text="删除学生信息", command=lambda: delete_student(index, detail_window))
    delete_button.grid(row=5, column=1, padx=10, pady=10)
 
def show_all_students():
    # 显示所有学生信息
    all_students_window = tk.Toplevel()
    all_students_window.title("所有学生信息")
 
    for index, student in enumerate(students_data):
        student_frame = tk.Frame(all_students_window, padx=10, pady=5)
        student_frame.pack(anchor=tk.W)
 
        student_info = f"姓名: {student['姓名']} - 学号: {student['学号']} - 年龄: {student['年龄']} - 联系方式: {student['联系方式']} - 专业名称: {student['专业名称']}"
        tk.Label(student_frame, text=student_info).pack(side=tk.LEFT)
 
        # 删除按钮
        delete_button = tk.Button(student_frame, text="删除", command=lambda idx=index: delete_student(idx, all_students_window))
        delete_button.pack(side=tk.RIGHT, padx=5)
 
    # 输入框和按钮用于输入学号并查找学生信息
    tk.Label(all_students_window, text="输入要查找的学号:").pack(padx=10, pady=5)
    search_entry_all = tk.Entry(all_students_window, width=30)
    search_entry_all.pack(padx=10, pady=5)
 
    search_button_all = tk.Button(all_students_window, text="查找学生信息", command=lambda: search_student_by_id(search_entry_all.get(), all_students_window))
    search_button_all.pack(padx=10, pady=5)
 
def search_student_by_id(student_id, window):
    found_student = None
    for student in students_data:
        if student['学号'] == student_id:
            found_student = student
            break
 
    if found_student:
        # 创建新窗口显示详细信息和操作按钮
        global action_window  
        action_window = tk.Toplevel()
        action_window.title("学生信息操作")
 
        global name_entry, id_entry, age_entry, contact_entry, major_entry  # 声明全局变量
 
        # 姓名
        tk.Label(action_window, text="姓名:").grid(row=0, column=0, padx=10, pady=5)
        name_var = tk.StringVar(action_window, value=found_student["姓名"])
        name_entry = tk.Entry(action_window, textvariable=name_var)
        name_entry.grid(row=0, column=1, padx=10, pady=5)
 
        # 学号
        tk.Label(action_window, text="学号:").grid(row=1, column=0, padx=10, pady=5)
        id_var = tk.StringVar(action_window, value=found_student["学号"])
        id_entry = tk.Entry(action_window, textvariable=id_var, state='disabled')  # 学号不可编辑
        id_entry.grid(row=1, column=1, padx=10, pady=5)
 
        # 年龄
        tk.Label(action_window, text="年龄:").grid(row=2, column=0, padx=10, pady=5)
        age_var = tk.StringVar(action_window, value=str(found_student["年龄"]))
        age_entry = tk.Entry(action_window, textvariable=age_var)
        age_entry.grid(row=2, column=1, padx=10, pady=5)
 
        # 联系方式
        tk.Label(action_window, text="联系方式:").grid(row=3, column=0, padx=10, pady=5)
        contact_var = tk.StringVar(action_window, value=found_student["联系方式"])
        contact_entry = tk.Entry(action_window, textvariable=contact_var)
        contact_entry.grid(row=3, column=1, padx=10, pady=5)
 
        # 专业名称
        tk.Label(action_window, text="专业名称:").grid(row=4, column=0, padx=10, pady=5)
        major_var = tk.StringVar(action_window, value=found_student["专业名称"])
        major_entry = tk.Entry(action_window, textvariable=major_var)
        major_entry.grid(row=4, column=1, padx=10, pady=5)
 
        # 更新按钮
        update_button = tk.Button(action_window, text="更新学生信息", command=lambda: update_student_detail(students_data.index(found_student), name_var.get(), id_var.get(), age_var.get(), contact_var.get(), major_var.get(), action_window))
        update_button.grid(row=5, column=0, padx=10, pady=10)
 
        # 删除按钮
        delete_button = tk.Button(action_window, text="删除学生信息", command=lambda: delete_student(students_data.index(found_student), action_window))
        delete_button.grid(row=5, column=1, padx=10, pady=10)
    else:
        messagebox.showinfo("提示", f"未找到学号为 {student_id} 的学生")
 
# 创建主窗口
root = tk.Tk()
root.title("学生信息管理系统")
 
# 加载学生数据
load_students_data()
 
# 学生信息输入框和按钮
name_label = tk.Label(root, text="姓名:")
name_label.grid(row=0, column=0, padx=10, pady=5)
 
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=10, pady=5)
 
id_label = tk.Label(root, text="学号:")
id_label.grid(row=1, column=0, padx=10, pady=5)
 
id_entry = tk.Entry(root)
id_entry.grid(row=1, column=1, padx=10, pady=5)
 
age_label = tk.Label(root, text="年龄:")
age_label.grid(row=2, column=0, padx=10, pady=5)
 
age_entry = tk.Entry(root)
age_entry.grid(row=2, column=1, padx=10, pady=5)
 
contact_label = tk.Label(root, text="联系方式:")
contact_label.grid(row=3, column=0, padx=10, pady=5)
 
contact_entry = tk.Entry(root)
contact_entry.grid(row=3, column=1, padx=10, pady=5)
 
major_label = tk.Label(root, text="专业名称:")
major_label.grid(row=4, column=0, padx=10, pady=5)
 
major_entry = tk.Entry(root)
major_entry.grid(row=4, column=1, padx=10, pady=5)
 
add_button = tk.Button(root, text="添加学生信息", command=add_student)
add_button.grid(row=5, column=0, columnspan=2, padx=10, pady=10)
 
# 学生信息展示列表
student_listbox = tk.Listbox(root, width=80, height=10)
student_listbox.grid(row=0, column=2, rowspan=6, padx=20, pady=10)
student_listbox.bind("<<ListboxSelect>>", lambda event: show_student_info())
 
# 显示所有学生信息按钮
show_all_button = tk.Button(root, text="显示所有学生信息", command=show_all_students)
show_all_button.grid(row=6, column=0, columnspan=3, padx=10, pady=10)
 
# 输入框和按钮用于输入学号并查找学生信息
search_label = tk.Label(root, text="输入学号查找学生:")
search_label.grid(row=7, column=0, padx=10, pady=5)
 
search_entry = tk.Entry(root)
search_entry.grid(row=7, column=1, padx=10, pady=5)
 
search_button = tk.Button(root, text="查找学生信息", command=lambda: search_student_by_id(search_entry.get(), root))
search_button.grid(row=7, column=2, padx=10, pady=5)
 
# 更新学生列表框内容
update_student_listbox()
 
root.mainloop()