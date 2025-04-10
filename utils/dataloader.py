import os
from colorama import Fore, Style
import torchvision.transforms as transforms
import torchvision.datasets as datasets

def datainfo(logger, args):

    if args.dataset == 'CIFAR10':
        print(Fore.YELLOW+'*'*80)
        logger.debug('CIFAR10')
        print('*'*80 + Style.RESET_ALL)
        n_classes = 10
        img_mean, img_std = (0.4914, 0.4822, 0.4465), (0.2470, 0.2435, 0.2616)
        img_size = 32        
        
    elif args.dataset == 'CIFAR100':
        print(Fore.YELLOW+'*'*80)
        logger.debug('CIFAR100')
        print('*'*80 + Style.RESET_ALL)
        n_classes = 100
        img_mean, img_std = (0.5070, 0.4865, 0.4409), (0.2673, 0.2564, 0.2762) 
        img_size = 32 
             
    elif args.dataset == 'T-IMNET':
        print(Fore.YELLOW+'*'*80)
        logger.debug('T-IMNET')
        print('*'*80 + Style.RESET_ALL)
        n_classes = 200
        img_mean, img_std = (0.4802, 0.4481, 0.3975), (0.2770, 0.2691, 0.2821)
        img_size = 64
        
    data_info = dict()
    data_info['n_classes'] = n_classes
    data_info['stat'] = (img_mean, img_std)
    data_info['img_size'] = img_size
    
    return data_info

def dataload(args, augmentations, normalize, data_info):
    if args.dataset == 'CIFAR10':
        train_dataset = datasets.CIFAR10(
            root=os.path.join(args.data_path,'cifar-10'), train=True, download=True, transform=augmentations)
        val_dataset = datasets.CIFAR10(
            root=os.path.join(args.data_path,'cifar-10'), train=False, download=True, transform=transforms.Compose([
            transforms.Resize(data_info['img_size']),
            transforms.ToTensor(),
            *normalize]))
        
    elif args.dataset == 'CIFAR100':

        train_dataset = datasets.CIFAR100(
            root=os.path.join(args.data_path,'cifar-100'), train=True, download=True, transform=augmentations)
        val_dataset = datasets.CIFAR100(
            root=os.path.join(args.data_path,'cifar-100'), train=False, download=True, transform=transforms.Compose([
            transforms.Resize(data_info['img_size']),
            transforms.ToTensor(),
            *normalize]))
        
    elif args.dataset == 'T-IMNET':
        train_dataset = datasets.ImageFolder(
            root=os.path.join(args.data_path, 'tiny-imagenet-200', 'train'), transform=augmentations)
        val_dataset = datasets.ImageFolder(
            root=os.path.join(args.data_path, 'tiny-imagenet-200', 'val'), 
            transform=transforms.Compose([
            transforms.Resize(data_info['img_size']), transforms.ToTensor(), *normalize]))
    
    return train_dataset, val_dataset
