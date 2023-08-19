class FilterModule(object):
    def filters(self):
        return {
            'list_cloudinit_files': self.list_cloudinit_files,
        }

    def list_cloudinit_files(self, kvm_vms):
        file_objects = []
        for vm in kvm_vms:
            if 'cloudinit' in vm and vm['cloudinit'].get('enabled', False):
                vm_name = vm['name']
                cloudinit_files = vm['cloudinit']['files']
                for file_name, file_content in cloudinit_files.items():
                    file_objects.append({
                        'host': vm_name,
                        'file': file_name,
                        'content': file_content.strip(),
                    })
        return file_objects
