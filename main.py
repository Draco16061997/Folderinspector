import config
import File
import BD


folder = File.Folder(config.path)
bd = BD.AddBD(config.db)

bd.writheBd(folder.getListFiles())


# bd = AddBD(config.db)
#     folder = File.Folder(config.path)
#     bd.writheBd(folder.getListFiles())


if __name__ == '__main__':
    None